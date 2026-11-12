# Play-Annotation-Generator Annotation Review — SplitZone_74

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_74`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 106
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 6
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | DT1 | defense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | DE2 | defense | `9` | `9` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `10` | `10` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 7 | START | 8 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 7 | START | 8 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `15` | `Group` | 7 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 7 | START | 8 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `4` | `Group` | 7 | START | 8 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `5` | `Group` | 7 | START | 8 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 7 | START | 8 | 43 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 7 | START | 8 | 113 |
| ✅ EXACT | `Action_BallSnap` | DT1 | `13` | `13` | 99 | START | 99 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE2 | `5` | `5` | 103 | START | 103 | 112 |
| ✅ EXACT | `Action_SnapReceive` | DE2 | `9` | `9` | 112 | END | 99 | 112 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `14` | `14` | 112 | START | 112 | 151 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `3` | `3` | 112 | START | 112 | 177 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `4` | `4` | 112 | START | 112 | 129 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `6` | `6` | 112 | START | 112 | 177 |
| ✅ EXACT | `Action_Handoff` | QB | `8` | `8` | 114 | START | 114 | 123 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `10` | `10` | 124 | START | 124 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 177 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 8–155
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 113 | 106 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 123 | 10 | inferred_complete_timeline |
| `Action_None` | 124 | 155 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–171
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 123 | 116 | inferred_complete_timeline |
| `Action_BallCarry` | 124 | 144 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 171 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 8–269
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 114 | 16 | inferred_complete_timeline |
| `Action_None` | 117 | 121 | 5 | inferred_complete_timeline |
| `Action_None` | 123 | 168 | 46 | inferred_complete_timeline |
| `Action_None` | 171 | 219 | 49 | inferred_complete_timeline |
| `Action_None` | 258 | 269 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 8–180
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 102 | 95 | inferred_complete_timeline |
| `Action_SplitBlock` | 103 | 112 | 10 | inferred_complete_timeline |
| `Action_SplitBlock` | 114 | 139 | 26 | inferred_complete_timeline |
| `Action_SplitBlock` | 144 | 168 | 25 | inferred_complete_timeline |
| `Action_SplitBlock` | 170 | 177 | 8 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–208
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 43 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 46 | 111 | 66 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 177 | 66 | inferred_complete_timeline |
| `Action_None` | 178 | 208 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 8–157
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 111 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 129 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 155 | 157 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–214
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 111 | 104 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 177 | 66 | inferred_complete_timeline |
| `Action_None` | 178 | 214 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–151
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 106 | 99 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 112 | 151 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 251

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 173 | 75 | inferred_complete_timeline |
| `Action_None` | 178 | 183 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 200 | 16 | inferred_complete_timeline |
| `Action_None` | 205 | 211 | 7 | inferred_complete_timeline |
| `Action_None` | 214 | 269 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–228
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_SnapReceive` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 113 | 228 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–227
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_BallSnap` | 99 | 112 | 14 | inferred_complete_timeline |
| `Action_None` | 113 | 168 | 56 | inferred_complete_timeline |
| `Action_None` | 170 | 208 | 39 | inferred_complete_timeline |
| `Action_None` | 212 | 227 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–130
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 130 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 8–145
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 145 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 8–183
- **Visible Samples:** 176

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 183 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 8–225
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 180 | 82 | inferred_complete_timeline |
| `Action_None` | 195 | 196 | 2 | inferred_complete_timeline |
| `Action_None` | 199 | 202 | 4 | inferred_complete_timeline |
| `Action_None` | 224 | 225 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–269
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_None` | 99 | 140 | 42 | inferred_complete_timeline |
| `Action_None` | 143 | 269 | 127 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 9–212 | 113 | 11 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 100–131 | 32 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 109–182 | 68 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 127–187 | 46 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 137–155 | 16 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 149–180 | 32 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 169–189 | 21 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 172–269 | 85 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 178–269 | 92 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 184–269 | 85 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 184–266 | 83 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 190–268 | 75 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 209–269 | 61 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 219–269 | 51 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 223–226 | 4 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 223–227 | 5 | 1 | Undefined position; Undefined team |
| `33` | `37` | Position_Unknown | Team_Unknown | 245–269 | 25 | 1 | Undefined position; Undefined team |
| `34` | `38` | Position_Unknown | Team_Unknown | 251–269 | 19 | 1 | Undefined position; Undefined team |
| `35` | `39` | Position_Unknown | Team_Unknown | 256–257 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `5` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `4` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ 20 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 20 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 40 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 150: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action 'Action_None' range [99-145] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-180] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-202] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-225] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-183] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-214] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [155-157] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [103-112] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [114-139] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SplitBlock' range [144-168] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-208] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-155] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-228] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [124-144] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-211] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-130] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-168] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-208] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-227] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-106] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [112-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-114] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-121] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-168] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-66] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [68-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-74] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-85] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-92] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 99, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [99-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-183] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-212] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-131] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-167] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-182] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-128] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-187] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-148] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-155] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-189] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-266] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-245] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-268] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-194] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-226] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-227] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '35' has 1 frames without a visible bounding box.
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

</details>