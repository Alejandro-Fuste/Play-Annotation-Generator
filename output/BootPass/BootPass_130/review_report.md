# Play-Annotation-Generator Annotation Review — BootPass_130

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_130`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 54
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 202
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 2
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 105
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `10` | `10` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | Team_Unknown | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `10` | `10` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `18` | `18` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `10` | `10` | 41 | END | 41 | 41 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `10` | `10` | 48 | START | 48 | 59 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | Position_Unknown | `10` | `10` | 60 | START | 60 | 71 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunFlatRoute` | Position_Unknown | `4` | `4` | 74 | START | 74 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_ThrowPass` | Position_Unknown | `10` | `10` | 145 | START | 145 | 148 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | Position_Unknown | `18` | `18` | 180 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

*(No offensive player tracks)*

</details>

<details>
<summary><strong>Defense</strong></summary>

*(No defensive player tracks)*

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `0` | Position_Unknown | Team_Unknown | 0–103 | 95 | 2 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–84 | 85 | 1 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–143 | 144 | 1 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–67 | 68 | 1 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–115 | 115 | 3 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–123 | 121 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–145 | 94 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–148 | 102 | 2 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–117 | 118 | 1 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–174 | 147 | 5 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–157 | 138 | 10 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–248 | 235 | 2 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–329 | 308 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–131 | 113 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 0–85 | 86 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 0–97 | 84 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 0–66 | 67 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–156 | 107 | 7 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 6–37 | 26 | 4 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 60–329 | 197 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 61–125 | 46 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 78–136 | 59 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 82–176 | 93 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 84–110 | 21 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 87–92 | 6 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 100–189 | 79 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 102–161 | 60 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 110–302 | 193 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 112–186 | 60 | 3 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 115–131 | 17 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 116–151 | 36 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 121–326 | 181 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 130–138 | 9 | 1 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 140–217 | 78 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 151–190 | 37 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 151–329 | 179 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 155–329 | 175 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 159–329 | 171 | 1 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 163–329 | 157 | 3 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 163–183 | 21 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 166–329 | 164 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 175–329 | 154 | 2 | Undefined position; Undefined team |
| `43` | `54` | Position_Unknown | Team_Unknown | 175–329 | 155 | 1 | Undefined position; Undefined team |
| `44` | `56` | Position_Unknown | Team_Unknown | 179–329 | 151 | 1 | Undefined position; Undefined team |
| `45` | `58` | Position_Unknown | Team_Unknown | 229–255 | 22 | 2 | Undefined position; Undefined team |
| `46` | `59` | Position_Unknown | Team_Unknown | 248–253 | 6 | 1 | Undefined position; Undefined team |
| `47` | `60` | Position_Unknown | Team_Unknown | 273–274 | 2 | 1 | Undefined position; Undefined team |
| `48` | `62` | Position_Unknown | Team_Unknown | 281–329 | 45 | 2 | Undefined position; Undefined team |
| `49` | `64` | Position_Unknown | Team_Unknown | 295–322 | 22 | 3 | Undefined position; Undefined team |
| `50` | `66` | Position_Unknown | Team_Unknown | 302–316 | 12 | 2 | Undefined position; Undefined team |
| `51` | `67` | Position_Unknown | Team_Unknown | 311–329 | 17 | 3 | Undefined position; Undefined team |
| `52` | `68` | Position_Unknown | Team_Unknown | 317–329 | 12 | 2 | Undefined position; Undefined team |
| `53` | `69` | Position_Unknown | Team_Unknown | 325–329 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BootAway` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunFlatRoute` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ThrowPass` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_SecureCatch` on target `18` (Position_Unknown)

### Track Identity Issues

- ⚠️ 54 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 54 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 33 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 108 |
| Missing visible bounding boxes during action | 91 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Segment 'Action_SecureCatch' for track '18' has invalid range: start=180, end=37. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-84] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [74-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunFlatRoute' range [113-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-148] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-76] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-96] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-157] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-169] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [60-71] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [90-110] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [145-148] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-157] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [72-248] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [58-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-131] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-74] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-97] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-9] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-21] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-121] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-156] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-15] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [19-20] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-25] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-37] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [60-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-78] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-99] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-125] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-136] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [82-88] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-90] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-110] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-146] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-189] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [102-161] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-302] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [112-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-158] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-186] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [115-131] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-151] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-278] for track '31' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [283-295] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [297-303] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-326] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-138] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-160] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-190] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-161] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-207] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-248] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-183] for track '40' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-181] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-329] for track '42' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-246] for track '45' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [252-255] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [248-253] for track '46' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [273-274] for track '47' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-317] for track '48' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [295-297] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-306] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-322] for track '49' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-316] for track '50' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-318] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [320-326] for track '51' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [317-320] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [322-329] for track '52' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '3' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '3' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '10' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '10' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '53' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '53' has undefined team_side. Will map to Team_Unknown.

</details>