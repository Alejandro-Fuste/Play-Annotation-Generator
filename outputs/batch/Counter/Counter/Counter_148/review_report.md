# Play-Annotation-Generator Annotation Review — Counter_148

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_148`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 37
- **Ball Tracks:** 0
- **Action Segments:** 134
- **Validation Warnings:** 149
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 99
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LG | offense | `2` | `1` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `13` | `12` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `14` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `1` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `2` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `4` | `Group` | 0 | START | 0 | 111 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 0 | START | 0 | 115 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 120 |
| ✅ EXACT | `Action_BallSnap` | LG | `2` | `1` | 112 | START | 112 | 115 |
| ✅ EXACT | `Action_DownBlock` | RG | `1` | `0` | 116 | START | 116 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `17` | 116 | START | 122 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `6` | `5` | 116 | START | 116 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `2` | `1` | 116 | START | 116 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `13` | `12` | 116 | START | 116 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `14` | 116 | END | 112 | 116 |
| ✅ EXACT | `Action_Handoff` | QB | `15` | `14` | 144 | START | 144 | 154 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 155 | START | 155 | 200 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 196 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_SnapReceive` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 117 | 143 | 27 | inferred_complete_timeline |
| `Action_Handoff` | 144 | 154 | 11 | inferred_complete_timeline |
| `Action_None` | 155 | 207 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–270
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 123 | 154 | 32 | inferred_complete_timeline |
| `Action_BallCarry` | 155 | 200 | 46 | inferred_complete_timeline |
| `Action_BallCarry` | 202 | 264 | 63 | inferred_complete_timeline |
| `Action_BallCarry` | 266 | 270 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 149 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–298
- **Visible Samples:** 255

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 150 | 39 | inferred_complete_timeline |
| `Action_None` | 152 | 228 | 77 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 234 | 235 | 2 | inferred_complete_timeline |
| `Action_None` | 237 | 249 | 13 | inferred_complete_timeline |
| `Action_None` | 251 | 258 | 8 | inferred_complete_timeline |
| `Action_None` | 297 | 298 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 116 | 170 | 55 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 172 | 196 | 25 | inferred_complete_timeline |
| `Action_None` | 197 | 202 | 6 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–157
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_BallSnap` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_PullBlock` | 116 | 136 | 21 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 157 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 152 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–185
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_DownBlock` | 116 | 146 | 31 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 155 | 7 | inferred_complete_timeline |
| `Action_DownBlock` | 157 | 180 | 24 | inferred_complete_timeline |
| `Action_DownBlock` | 182 | 185 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 8 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 17 | 18 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 73 | 75 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 106 | 18 | inferred_complete_timeline |
| `Action_None` | 113 | 118 | 6 | inferred_complete_timeline |
| `Action_None` | 131 | 160 | 30 | inferred_complete_timeline |
| `Action_None` | 170 | 175 | 6 | inferred_complete_timeline |
| `Action_None` | 179 | 180 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 299 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 106 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 299 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 118 | 7 | inferred_complete_timeline |
| `Action_None` | 202 | 219 | 18 | inferred_complete_timeline |
| `Action_None` | 221 | 227 | 7 | inferred_complete_timeline |
| `Action_None` | 231 | 235 | 5 | inferred_complete_timeline |
| `Action_None` | 241 | 272 | 32 | inferred_complete_timeline |
| `Action_None` | 287 | 290 | 4 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–266
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 39 | 51 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 83 | 28 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 111 | 22 | inferred_complete_timeline |
| `Action_None` | 112 | 116 | 5 | inferred_complete_timeline |
| `Action_None` | 132 | 141 | 10 | inferred_complete_timeline |
| `Action_None` | 159 | 232 | 74 | inferred_complete_timeline |
| `Action_None` | 245 | 266 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |
| `Action_None` | 133 | 141 | 9 | inferred_complete_timeline |
| `Action_None` | 153 | 164 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–249
- **Visible Samples:** 250

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_None` | 112 | 249 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 11–128
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 11 | 111 | 101 | inferred_complete_timeline |
| `Action_None` | 112 | 128 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–299 | 211 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 122–299 | 151 | 5 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 135–299 | 108 | 10 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 146–213 | 51 | 4 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 162–299 | 132 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 170–187 | 18 | 1 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 170–176 | 7 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 177–243 | 38 | 4 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 200–299 | 100 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 200–211 | 12 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 210–299 | 80 | 3 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 215–299 | 77 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 225–299 | 75 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 228–299 | 69 | 3 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 228–235 | 8 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 231–299 | 69 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 244–299 | 47 | 5 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 244–266 | 22 | 2 | Undefined position; Undefined team |
| `34` | `41` | Position_Unknown | Team_Unknown | 247–299 | 38 | 4 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 257–269 | 12 | 2 | Undefined position; Undefined team |
| `36` | `44` | Position_Unknown | Team_Unknown | 296–299 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `6` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `16` (actor_track_id `17`): `SAF` position mapped to `defense` team
- ⚠️ 22 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 22 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 44 |
| Missing visible bounding boxes during action | 104 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Action 'Action_DownBlock' range [116-152] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [116-136] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-157] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-249] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-150] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-228] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-249] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [297-298] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-90] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-93] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-97] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-106] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [116-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [149-155] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [157-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [182-185] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-299] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-141] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-164] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [155-200] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [202-264] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [266-270] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-51] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-83] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-111] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-116] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-141] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-232] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-266] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [116-170] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-202] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-219] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-227] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-235] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-272] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-290] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-8] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [73-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-106] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-118] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-160] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-175] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-180] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [122-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-272] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [277-280] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-187] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-201] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-205] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [217-226] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-265] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [285-286] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-155] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-173] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-213] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-272] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-187] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-176] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-180] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-200] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-234] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-243] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-211] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-224] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-263] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-299] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-242] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [245-247] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-235] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-270] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-277] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [281-282] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-266] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-249] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-258] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [257-266] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>