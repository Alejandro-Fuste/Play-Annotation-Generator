# Play-Annotation-Generator Annotation Review — Counter_374

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_374`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 37
- **Ball Tracks:** 1
- **Action Segments:** 79
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 5
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `10` | `9` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `15` | `14` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `3` | `2` |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | offense | `17` | `16` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | offense | `12` | `11` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `12` | `Group` | 0 | START | 0 | 135 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `17` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 84 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 87 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 84 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `14` | 85 | START | 85 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `10` | `9` | 88 | START | 88 | 135 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `15` | `14` | 88 | START | 91 | 174 |
| ✅ EXACT | `Action_PullBlock` | RG | `3` | `2` | 88 | START | 88 | 174 |
| ✅ EXACT | `Action_PullLeadBlock` | RB2 | `17` | `16` | 88 | START | 88 | 174 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 90 | END | 85 | 90 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 114 | START | 114 | 135 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB1 | `12` | `11` | 136 | START | 136 | 139 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 174 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_SnapReceive` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_None` | 91 | 113 | 23 | inferred_complete_timeline |
| `Action_Handoff` | 114 | 135 | 22 | inferred_complete_timeline |
| `Action_None` | 136 | 174 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_BallCarry` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_BallCarry` | 141 | 269 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–215
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 88 | 174 | 87 | inferred_complete_timeline |
| `Action_None` | 175 | 215 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 174 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 213 | 129 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_DownBlock` | 88 | 135 | 48 | inferred_complete_timeline |
| `Action_DownBlock` | 142 | 174 | 33 | inferred_complete_timeline |
| `Action_None` | 175 | 226 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_BallSnap` | 85 | 90 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 91 | 174 | 84 | inferred_complete_timeline |
| `Action_None` | 175 | 202 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 87 | 88 | inferred_complete_timeline |
| `Action_PullBlock` | 88 | 174 | 87 | inferred_complete_timeline |
| `Action_None` | 175 | 204 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–194
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 194 | 110 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–178
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 167 | 83 | inferred_complete_timeline |
| `Action_None` | 170 | 173 | 4 | inferred_complete_timeline |
| `Action_None` | 177 | 178 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 151 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–211
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 168 | 84 | inferred_complete_timeline |
| `Action_None` | 171 | 211 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–200
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 200 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–247
- **Visible Samples:** 243

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 171 | 87 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 247 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 188 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 84 | 85 | inferred_complete_timeline |
| `Action_None` | 85 | 269 | 185 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 103–110 | 7 | 2 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 109–231 | 123 | 1 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 122–269 | 145 | 2 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 144–145 | 2 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 154–269 | 116 | 1 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 161–174 | 14 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 161–167 | 7 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 172–175 | 4 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 178–183 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 184–220 | 37 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 224–255 | 15 | 5 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 232–257 | 24 | 2 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 233–234 | 2 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 236–244 | 9 | 1 | Undefined position; Undefined team |
| `33` | `45` | Position_Unknown | Team_Unknown | 248–269 | 21 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 258–266 | 6 | 2 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 262–265 | 4 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 269–269 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `28` | `37` | 212 | 212 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `10` (2 segments found)
- ⚠️ `Action_DownBlock` for actor_track_id `15` (C): Annotated start 88 != Inferred start 91
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `12` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `5` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 48 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [85–90], lower_priority='Action_DownBlock' annotated_start=88, effective_Action_DownBlock_start=91.
- ⚠️ Action 'Action_PullBlock' range [88-174] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-171] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-247] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-151] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-213] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-167] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-188] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [88-135] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-226] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-174] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [136-139] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-168] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-211] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-200] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-202] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-194] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [88-174] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-215] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-174] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-106] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-110] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-156] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-174] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-183] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-220] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-226] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-245] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [253-255] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-248] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-257] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-244] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-261] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-265] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '36' has 1 frames without a visible bounding box.
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