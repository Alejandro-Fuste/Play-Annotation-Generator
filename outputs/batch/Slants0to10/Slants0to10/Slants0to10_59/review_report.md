# Play-Annotation-Generator Annotation Review — Slants0to10_59

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_59`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 114
- **Validation Warnings:** 132
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 4
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 91
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `13` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `19` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_PassBlock` | RT | `13` | `13` | 7 | START | 7 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `16` | `16` | 7 | START | 7 | 150 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 7 | START | 7 | 14 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 7 | START | 7 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `7` | `7` | 7 | START | 7 | 162 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 7 | END | 7 | 7 |
| ✅ EXACT | `Action_RunSlantRoute` | WR3 | `0` | `0` | 13 | START | 13 | 71 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 65 | START | 65 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR3 | `0` | `0` | 93 | START | 93 | 182 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 7 | 1 | inferred_complete_timeline |
| `Action_None` | 8 | 64 | 57 | inferred_complete_timeline |
| `Action_ThrowPass` | 65 | 73 | 9 | inferred_complete_timeline |
| `Action_None` | 74 | 195 | 122 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–204
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 106 | 107 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 115 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 182 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 184 | 204 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 13 | 71 | 59 | inferred_complete_timeline |
| `Action_None` | 72 | 92 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 93 | 182 | 90 | inferred_complete_timeline |
| `Action_BallCarry` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 196 | 201 | 6 | inferred_complete_timeline |
| `Action_BallCarry` | 204 | 207 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 162 | 156 | inferred_complete_timeline |
| `Action_PassBlock` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 190 | 239 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 150 | 144 | inferred_complete_timeline |
| `Action_PassBlock` | 196 | 202 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 14 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 16 | 73 | 58 | inferred_complete_timeline |
| `Action_PassBlock` | 78 | 150 | 73 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 154 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 81

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 66 | 60 | inferred_complete_timeline |
| `Action_PassBlock` | 72 | 85 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 45

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 7 | 44 | 38 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_PreSnap` | 181 | 239 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 25 | 26 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 31 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 125 | 88 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 173 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 179 | 192 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 136 | 137 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 149 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 239 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 44 | 157 | 114 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 175 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 158 | 159 | inferred_complete_timeline |
| `Action_PreSnap` | 164 | 165 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PreSnap` | 134 | 135 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 161 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 219 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 195 | 196 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 198 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 203 | 239 | 37 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 7–145 | 75 | 10 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 24–239 | 179 | 5 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 81–120 | 39 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 89–138 | 29 | 5 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 103–107 | 5 | 1 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 119–160 | 42 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 151–153 | 3 | 1 | Undefined position; Undefined team |
| `30` | `46` | Position_Unknown | Team_Unknown | 172–239 | 60 | 3 | Undefined position; Undefined team |
| `31` | `47` | Position_Unknown | Team_Unknown | 176–177 | 2 | 1 | Undefined position; Undefined team |
| `32` | `48` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `33` | `49` | Position_Unknown | Team_Unknown | 186–239 | 53 | 2 | Undefined position; Undefined team |
| `34` | `50` | Position_Unknown | Team_Unknown | 191–194 | 4 | 1 | Undefined position; Undefined team |
| `35` | `51` | Position_Unknown | Team_Unknown | 191–239 | 49 | 1 | Undefined position; Undefined team |
| `36` | `52` | Position_Unknown | Team_Unknown | 197–239 | 27 | 3 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 200–202 | 3 | 1 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 209–211 | 3 | 1 | Undefined position; Undefined team |
| `39` | `56` | Position_Unknown | Team_Unknown | 218–239 | 19 | 2 | Undefined position; Undefined team |
| `40` | `57` | Position_Unknown | Team_Unknown | 224–239 | 11 | 3 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 91 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [93-182] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [193-194] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [196-201] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [204-207] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-179] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-106] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-115] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-182] for track '4' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [184-204] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-25] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-31] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-125] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-173] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-192] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-162] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [164-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [177-178] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [180-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [190-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-136] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-149] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-160] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-161] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-219] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-62] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-135] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-158] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-44] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-195] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-195] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-150] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [196-202] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-175] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-14] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [16-73] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [78-150] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [7-66] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [72-85] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-8] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-15] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-23] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-36] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-45] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [54-95] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-100] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-111] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [144-145] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-160] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-165] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [207-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-117] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-93] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-138] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-107] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-160] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-153] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-179] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [185-232] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-177] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-217] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-194] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-239] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-202] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-220] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-202] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-211] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-233] for track '39' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-234] for track '40' has 2 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>