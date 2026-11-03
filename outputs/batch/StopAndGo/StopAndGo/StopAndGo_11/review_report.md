# Play-Annotation-Generator Annotation Review — StopAndGo_11

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_11`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 97
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 75
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_VerticalStem` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_SellStop` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `15` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `17` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `15` | `15` | 25 | START | 25 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `15` | `15` | 28 | START | 42 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `17` | `17` | 28 | START | 28 | 47 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 28 | START | 28 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 28 | START | 28 | 43 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `7` | `7` | 28 | START | 28 | 218 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 41 | END | 25 | 41 |
| ✅ EXACT | `Action_VerticalStem` | WR3 | `0` | `0` | 41 | START | 41 | 85 |
| ✅ EXACT | `Action_SellStop` | WR3 | `0` | `0` | 86 | START | 86 | 111 |
| ✅ EXACT | `Action_RunGoRoute` | WR3 | `0` | `0` | 112 | START | 112 | 239 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 125 | START | 125 | 136 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_None` | 42 | 124 | 83 | inferred_complete_timeline |
| `Action_ThrowPass` | 125 | 136 | 12 | inferred_complete_timeline |
| `Action_None` | 137 | 150 | 14 | inferred_complete_timeline |
| `Action_None` | 152 | 154 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 148 | 124 | inferred_complete_timeline |
| `Action_None` | 153 | 171 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 121 | 97 | inferred_complete_timeline |
| `Action_None` | 124 | 126 | 3 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_VerticalStem` | 41 | 85 | 45 | inferred_complete_timeline |
| `Action_SellStop` | 86 | 111 | 26 | inferred_complete_timeline |
| `Action_RunGoRoute` | 112 | 239 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 111 | 87 | inferred_complete_timeline |
| `Action_None` | 117 | 196 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 201 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 63 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 71 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–195
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 41 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 42 | 44 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 69 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 71 | 180 | 110 | inferred_complete_timeline |
| `Action_PassBlock` | 184 | 195 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–199
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 43 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 59 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 189 | 103 | inferred_complete_timeline |
| `Action_PassBlock` | 191 | 193 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 195 | 199 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 218 | 191 | inferred_complete_timeline |
| `Action_PassBlock` | 221 | 223 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–177
- **Visible Samples:** 178

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 177 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 73 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 51 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–196
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 175 | 151 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 196 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 107 | 83 | inferred_complete_timeline |
| `Action_None` | 111 | 188 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 109 | 85 | inferred_complete_timeline |
| `Action_None` | 116 | 239 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 226

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 189 | 165 | inferred_complete_timeline |
| `Action_None` | 194 | 200 | 7 | inferred_complete_timeline |
| `Action_None` | 211 | 239 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 230 | 206 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 239 | 215 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 38–194 | 154 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 67–144 | 77 | 2 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 72–126 | 25 | 4 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 109–118 | 10 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 110–120 | 11 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 124–177 | 54 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 162–239 | 72 | 5 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 166–187 | 22 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 170–205 | 36 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 214–239 | 26 | 1 | Undefined position; Undefined team |
| `33` | `48` | Position_Unknown | Team_Unknown | 226–235 | 9 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 226–239 | 9 | 3 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 229–239 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 63 |
| Track-related warning | 1 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_PassBlock' annotated_start=28, effective_Action_PassBlock_start=42.
- ⚠️ Action 'Action_RunGoRoute' range [112-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-230] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-109] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-177] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-73] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-111] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-196] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-218] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [221-223] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-121] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-189] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-200] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-239] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-51] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-175] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [42-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-69] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [71-180] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [184-195] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-154] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-47] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-201] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-107] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-188] for track '19' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-63] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-71] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-43] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-59] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-189] for track '21' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [191-193] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [195-199] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-194] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-141] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-73] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-76] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-98] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-118] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-177] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-200] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-209] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-223] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-226] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-187] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-205] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-232] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-229] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-233] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-239] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-231] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '35' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>