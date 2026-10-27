# Play-Annotation-Generator Annotation Review — Counter_96

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_96`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 110
- **Validation Warnings:** 118
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 1
- **Group Expanded Events:** 6
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 92
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | SAF | defense | `3` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | defense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `6` | `5` |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | DT3 | defense | `11` | `10` |
| ⚠️ END CHANGED | `Action_SnapReceive` | DT3 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT3 | defense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `12` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 86 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `7` | `Group` | 0 | START | 0 | 121 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 92 |
| ✅ EXACT | `Action_BallSnap` | SAF | `3` | `2` | 87 | START | 87 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DT1 | `15` | `14` | 93 | START | 93 | 109 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `9` | `8` | 93 | START | 93 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `6` | `5` | 93 | START | 93 | 110 |
| ❌ MISSING SEGMENT | `Action_PullLeadBlock` | DT3 | `11` | `10` | 93 | START | N/A | N/A |
| ⚠️ END CHANGED | `Action_SnapReceive` | DT3 | `11` | `10` | 102 | END | 87 | 101 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | DT3 | `11` | `10` | 108 | START | 108 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `7` | `6` | 130 | START | 131 | 141 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 176 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–147
- **Visible Samples:** 136

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_BallCarry` | 131 | 141 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 145 | 147 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–232
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 98 | 12 | inferred_complete_timeline |
| `Action_None` | 105 | 126 | 22 | inferred_complete_timeline |
| `Action_None` | 130 | 142 | 13 | inferred_complete_timeline |
| `Action_None` | 161 | 229 | 69 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 113 | 27 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 144 | 172 | 29 | inferred_complete_timeline |
| `Action_None` | 179 | 181 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 186 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 194 | 6 | inferred_complete_timeline |
| `Action_None` | 198 | 200 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 146 | 54 | inferred_complete_timeline |
| `Action_DownBlock` | 150 | 176 | 27 | inferred_complete_timeline |
| `Action_None` | 177 | 189 | 13 | inferred_complete_timeline |
| `Action_None` | 191 | 205 | 15 | inferred_complete_timeline |
| `Action_None` | 208 | 209 | 2 | inferred_complete_timeline |
| `Action_None` | 230 | 269 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PullBlock` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 144 | 176 | 33 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 198 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–217
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 119 | 33 | inferred_complete_timeline |
| `Action_None` | 209 | 213 | 5 | inferred_complete_timeline |
| `Action_None` | 215 | 217 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 119 | 33 | inferred_complete_timeline |
| `Action_None` | 123 | 166 | 44 | inferred_complete_timeline |
| `Action_None` | 171 | 200 | 30 | inferred_complete_timeline |
| `Action_None` | 265 | 269 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 140 | 54 | inferred_complete_timeline |
| `Action_None` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_None` | 149 | 269 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 109 | 17 | inferred_complete_timeline |
| `Action_DownBlock` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 248

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 111 | 25 | inferred_complete_timeline |
| `Action_None` | 114 | 249 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 87 | 101 | 15 | inferred_complete_timeline |
| `Action_None` | 103 | 107 | 5 | inferred_complete_timeline |
| `Action_Handoff` | 108 | 111 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 113 | 116 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 126 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–174
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 167 | 81 | inferred_complete_timeline |
| `Action_None` | 169 | 174 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_None` | 87 | 269 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 55–269
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 55 | 86 | 32 | inferred_complete_timeline |
| `Action_None` | 87 | 172 | 86 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 186 | 223 | 38 | inferred_complete_timeline |
| `Action_None` | 228 | 246 | 19 | inferred_complete_timeline |
| `Action_None` | 248 | 269 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 86 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 87 | 102 | 16 | inferred_complete_timeline |
| `Action_None` | 103 | 250 | 148 | inferred_complete_timeline |
| `Action_None` | 264 | 269 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `0` | `1` | Position_Unknown | Team_Unknown | 0–248 | 249 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 55–62 | 8 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 93–269 | 150 | 6 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 117–269 | 136 | 6 | Undefined position; Undefined team |
| `19` | `22` | Position_Unknown | Team_Unknown | 118–269 | 147 | 2 | Undefined position; Undefined team |
| `20` | `23` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 134–269 | 123 | 4 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 144–155 | 12 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 146–168 | 23 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 196–269 | 73 | 2 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 206–269 | 62 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 218–228 | 11 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 224–250 | 20 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 228–259 | 29 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 230–269 | 40 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 230–260 | 30 | 2 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 233–269 | 37 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (3 segments found)
- ❌ Missing segment for action `Action_PullLeadBlock` on target `11` (DT3)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `11` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ 18 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 18 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 36 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 194: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_PullLeadBlock' for track '10' has invalid range: start=93, end=86. Clamping end to start.
- ⚠️ Action 'Action_None' range [87-248] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-166] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-200] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-269] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-250] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-172] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-194] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-111] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-249] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [93-110] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [112-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-198] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [131-141] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [145-147] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-146] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-189] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-205] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-167] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [87-101] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [108-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [113-116] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [118-126] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-98] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-126] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-142] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-229] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-140] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-119] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-213] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-217] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-109] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [113-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-223] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-246] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [55-62] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-136] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-259] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-135] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-228] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-238] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-269] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-191] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-151] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-192] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-155] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-261] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-269] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-218] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-228] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-237] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-246] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-259] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-256] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-260] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '0' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '0' has undefined team_side. Will map to Team_Unknown.
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