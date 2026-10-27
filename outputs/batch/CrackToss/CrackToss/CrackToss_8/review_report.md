# Play-Annotation-Generator Annotation Review — CrackToss_8

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_8`
- **Frame Range:** 0 to 328 (329 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Tackle`
- **Result Frame:** 328
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 126
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 4
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 94
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | Team_Unknown | `20` | `17` |
| ✅ EXACT | `Action_PullBlock` | LT | offense | `1` | `0` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | Team_Unknown | `22` | `18` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `4` | `Group` | 0 | START | 0 | 112 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 147 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 112 |
| ⚠️ START CHANGED | `Action_BallSnap` | Position_Unknown | `20` | `17` | 113 | START | 115 | 115 |
| ✅ EXACT | `Action_PullBlock` | LT | `1` | `0` | 114 | START | 114 | 219 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 115 | END | 113 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | Position_Unknown | `22` | `18` | 126 | START | 126 | 151 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 126 | START | 126 | 147 |
| ✅ EXACT | `Action_BallCarry` | RB | `5` | `4` | 148 | START | 148 | 235 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 219 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_SnapReceive` | 113 | 115 | 3 | inferred_complete_timeline |
| `Action_None` | 116 | 125 | 10 | inferred_complete_timeline |
| `Action_Toss` | 126 | 147 | 22 | inferred_complete_timeline |
| `Action_None` | 148 | 191 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 147 | 148 | inferred_complete_timeline |
| `Action_BallCarry` | 148 | 235 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–189
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 146 | 34 | inferred_complete_timeline |
| `Action_None` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |
| `Action_None` | 181 | 189 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–328
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 113 | 103 | inferred_complete_timeline |
| `Action_PullBlock` | 114 | 219 | 106 | inferred_complete_timeline |
| `Action_None` | 220 | 328 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 165 | 53 | inferred_complete_timeline |
| `Action_None` | 169 | 171 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–321
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 296 | 184 | inferred_complete_timeline |
| `Action_None` | 298 | 313 | 16 | inferred_complete_timeline |
| `Action_None` | 315 | 321 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_None` | 149 | 161 | 13 | inferred_complete_timeline |
| `Action_None` | 164 | 172 | 9 | inferred_complete_timeline |
| `Action_None` | 177 | 233 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–283
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 187 | 75 | inferred_complete_timeline |
| `Action_None` | 189 | 224 | 36 | inferred_complete_timeline |
| `Action_None` | 231 | 244 | 14 | inferred_complete_timeline |
| `Action_None` | 248 | 283 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–40
- **Visible Samples:** 41

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–240
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 33 | 34 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 43 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 112 | 66 | inferred_complete_timeline |
| `Action_None` | 113 | 121 | 9 | inferred_complete_timeline |
| `Action_None` | 128 | 180 | 53 | inferred_complete_timeline |
| `Action_None` | 184 | 229 | 46 | inferred_complete_timeline |
| `Action_None` | 231 | 240 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–42
- **Visible Samples:** 43

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 42 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 142 | 30 | inferred_complete_timeline |
| `Action_None` | 144 | 159 | 16 | inferred_complete_timeline |
| `Action_None` | 223 | 249 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 128 | 16 | inferred_complete_timeline |
| `Action_None` | 132 | 133 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 21 | 112 | 92 | inferred_complete_timeline |
| `Action_None` | 113 | 139 | 27 | inferred_complete_timeline |
| `Action_None` | 144 | 151 | 8 | inferred_complete_timeline |
| `Action_None` | 156 | 220 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–328
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_None` | 113 | 186 | 74 | inferred_complete_timeline |
| `Action_None` | 188 | 202 | 15 | inferred_complete_timeline |
| `Action_None` | 206 | 221 | 16 | inferred_complete_timeline |
| `Action_None` | 226 | 235 | 10 | inferred_complete_timeline |
| `Action_None` | 237 | 245 | 9 | inferred_complete_timeline |
| `Action_None` | 248 | 265 | 18 | inferred_complete_timeline |
| `Action_None` | 268 | 328 | 61 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `17` | Position_Unknown | Team_Unknown | 4–27 | 24 | 1 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 47–180 | 84 | 3 | Undefined position; Undefined team |
| `17` | `20` | Position_Unknown | Team_Unknown | 115–256 | 114 | 6 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 126–243 | 91 | 5 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 131–257 | 126 | 2 | Undefined position; Undefined team |
| `20` | `24` | Position_Unknown | Team_Unknown | 132–273 | 122 | 4 | Undefined position; Undefined team |
| `21` | `25` | Position_Unknown | Team_Unknown | 139–296 | 144 | 4 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 143–259 | 89 | 4 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 144–168 | 25 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 147–249 | 80 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 168–328 | 154 | 2 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 171–266 | 83 | 3 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 184–328 | 116 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 199–206 | 8 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 212–256 | 40 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 242–275 | 33 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 261–273 | 13 | 1 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 323–327 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_BallSnap` for actor_track_id `20` (Position_Unknown): Annotated start 113 != Inferred start 115
- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `22` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 88 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '0' (LT) duration 106 frames exceeds threshold 90 frames [start=114, end=219].
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-296] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [298-313] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-321] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-42] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-165] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [148-235] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-189] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-202] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-221] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-235] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-245] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-265] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-187] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-224] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-244] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-283] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-249] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-139] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-161] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-172] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-33] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-43] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-121] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-180] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-229] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-240] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-139] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-151] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-191] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-27] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-180] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-158] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-197] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [126-151] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [172-180] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-146] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-257] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-195] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-228] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-273] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-161] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-296] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-214] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-259] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-168] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-184] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-212] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-249] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-242] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-197] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-221] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-266] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-208] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-302] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [324-328] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-206] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-217] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-256] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-275] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-273] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-327] for track '32' has 1 frames without a visible bounding box.
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

</details>