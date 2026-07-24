function decodeURI(s)
    s = string.gsub(s, '%%(%x%x)', function(h) return string.char(tonumber(h, 16)) end)
    return s
end

function encodeURI(s)
    s = string.gsub(s, "([^%w%.%- ])", function(c) return string.format("%%%02X", string.byte(c)) end)
    return string.gsub(s, " ", "+")
end

function on_pause_change(name, value)
    if value == true then
        print("@PT");
    else
        print("@PF")
    end
end

function on_seeking_change(name, value)
    if value == true then
        print("@SKG");
    else
        print("@SKD")
    end
end

function on_seek()
    if mp.get_property("time-pos") ~= nil then
		print( "@SK>"..mp.get_property("time-pos"))
	end
end

function on_time_change(name, value)
	if value ~= nil then
		print("@TC>"..value)
	end
end

function on_duration_change(name, value)
	if value ~= nil then
		print("@MD>"..value)
	end
end

function on_speed_change(name, value)
	if value ~= nil then
		print("@SC>"..value)
	end
end

function on_volume_change(name, value)
	if value ~= nil then
		print("@VC>"..value)
	end
end

function on_path_change(name, value)
	if value ~= nil then
		print("@MPC>"..value)
	end
end

mp.register_event("seek", on_seek)
mp.observe_property("pause", "bool", on_pause_change)
mp.observe_property("seeking", "bool", on_seeking_change)
mp.observe_property("time-pos", "number", on_time_change)
mp.observe_property("duration", "number", on_duration_change)
mp.observe_property("speed", "number", on_speed_change)
mp.observe_property("volume", "number", on_volume_change)
mp.observe_property("path", "string", on_path_change)

--load done
print("@ALLD")