# Play-Annotation-Generator Annotation Review — BootPass_84

**Overall Status:** FAILED

## 1. Clip & Validation Summary

- **Video:** `BootPass_84`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 121
- **Validation Warnings:** 173
- **Validation Errors:** 2
- **Overall Status:** FAILED

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 7
- **Exact Matches:** 6
- **Group Expanded Events:** 0
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 115
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | Team_Unknown | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | Team_Unknown | `3` | `3` |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | Team_Unknown | `34` | `31` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `3` | `3` | 103 | END | 103 | 103 |
| ✅ EXACT | `Action_FakeHandoff` | Position_Unknown | `3` | `3` | 108 | START | 108 | 140 |
| ✅ EXACT | `Action_BootAway` | Position_Unknown | `3` | `3` | 141 | START | 141 | 173 |
| ✅ EXACT | `Action_RunFlatRoute` | Position_Unknown | `15` | `15` | 141 | START | 141 | 142 |
| ✅ EXACT | `Action_ThrowPass` | Position_Unknown | `3` | `3` | 177 | START | 177 | 187 |
| ✅ EXACT | `Action_SecureCatch` | Position_Unknown | `34` | `31` | 226 | START | 226 | 241 |

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
| `0` | `0` | Position_Unknown | Team_Unknown | 0–329 | 298 | 3 | Undefined position; Undefined team |
| `1` | `1` | Position_Unknown | Team_Unknown | 0–329 | 313 | 7 | Undefined position; Undefined team |
| `2` | `2` | Position_Unknown | Team_Unknown | 0–281 | 276 | 3 | Undefined position; Undefined team |
| `3` | `3` | Position_Unknown | Team_Unknown | 0–329 | 330 | 8 | Undefined position; Undefined team |
| `4` | `4` | Position_Unknown | Team_Unknown | 0–181 | 178 | 2 | Undefined position; Undefined team |
| `5` | `5` | Position_Unknown | Team_Unknown | 0–223 | 223 | 2 | Undefined position; Undefined team |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–329 | 328 | 2 | Undefined position; Undefined team |
| `7` | `7` | Position_Unknown | Team_Unknown | 0–329 | 297 | 7 | Undefined position; Undefined team |
| `8` | `8` | Position_Unknown | Team_Unknown | 0–329 | 303 | 9 | Undefined position; Undefined team |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–204 | 205 | 1 | Undefined position; Undefined team |
| `10` | `10` | Position_Unknown | Team_Unknown | 0–329 | 253 | 3 | Undefined position; Undefined team |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–329 | 237 | 7 | Undefined position; Undefined team |
| `12` | `12` | Position_Unknown | Team_Unknown | 2–140 | 129 | 2 | Undefined position; Undefined team |
| `13` | `13` | Position_Unknown | Team_Unknown | 4–146 | 131 | 3 | Undefined position; Undefined team |
| `14` | `14` | Position_Unknown | Team_Unknown | 9–146 | 20 | 5 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 126–166 | 41 | 3 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 132–139 | 4 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 134–329 | 193 | 4 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 148–329 | 180 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 169–196 | 6 | 2 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 169–170 | 2 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 180–241 | 58 | 3 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 183–329 | 136 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 184–185 | 2 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 189–329 | 141 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 191–285 | 11 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 200–329 | 126 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 202–329 | 128 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 202–322 | 118 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 205–329 | 120 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 209–328 | 113 | 4 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 210–328 | 112 | 4 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 223–249 | 27 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 227–329 | 101 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 258–329 | 66 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 263–329 | 55 | 2 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 272–317 | 11 | 3 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 306–329 | 24 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ 38 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 38 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

- ❌ Group/position target 'ALL' for action 'Action_PreSnap' at frame 0 could not be resolved to any XML tracks (position/team_side missing).
- ❌ Group/position target 'OL' for action 'Action_RunBlock' at frame 93 could not be resolved to any XML tracks (position/team_side missing).

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 76 |
| Missing visible bounding boxes during action | 95 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-119] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-307] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-132] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-241] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [245-278] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-167] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-221] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-281] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-181] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-219] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [221-223] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-238] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-174] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-225] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-187] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-223] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-230] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [242-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-253] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [255-262] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-329] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-204] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-164] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-207] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [214-265] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [268-270] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-273] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-128] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-128] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-142] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-146] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-12] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-92] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-102] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-139] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-296] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-322] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [324-329] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-249] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [251-298] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [193-196] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-187] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-241] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-222] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-289] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [300-329] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-185] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-329] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-195] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [280-285] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-240] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-296] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [298-299] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [301-317] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [319-322] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-308] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [311-314] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-321] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-300] for track '30' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-307] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [313-323] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [325-328] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-319] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [327-328] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [227-284] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [258-272] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [278-306] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [263-288] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [272-276] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [281-284] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [316-317] for track '36' has 1 frames without a visible bounding box.
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

</details>