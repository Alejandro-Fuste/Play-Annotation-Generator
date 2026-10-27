# Play-Annotation-Generator Annotation Review — Counter_103

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_103`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | defense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `7` | `6` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `13` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `22` | `Group` | 0 | START | 0 | 19 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 73 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 73 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `8` | 74 | START | 74 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RG | `13` | `12` | 75 | START | 75 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | DE2 | `20` | `19` | 75 | START | 75 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `9` | `8` | 75 | START | 85 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `16` | `15` | 75 | START | 75 | 88 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `14` | `13` | 75 | START | 75 | 87 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 84 | END | 74 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `7` | `6` | 101 | START | 101 | 117 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 159 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_SnapReceive` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_None` | 85 | 100 | 16 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 117 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–237
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 27 | 59 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 73 | 11 | inferred_complete_timeline |
| `Action_None` | 74 | 79 | 6 | inferred_complete_timeline |
| `Action_None` | 84 | 85 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 218 | 125 | inferred_complete_timeline |
| `Action_None` | 235 | 237 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 141 | 68 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 215 | 142 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–221
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 221 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 173

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 160 | 87 | inferred_complete_timeline |
| `Action_None` | 164 | 175 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 90 | 151 | 62 | inferred_complete_timeline |
| `Action_None` | 165 | 166 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 194 | 26 | inferred_complete_timeline |
| `Action_None` | 197 | 211 | 15 | inferred_complete_timeline |
| `Action_None` | 214 | 239 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PullBlock` | 75 | 88 | 14 | inferred_complete_timeline |
| `Action_PullBlock` | 94 | 137 | 44 | inferred_complete_timeline |
| `Action_PullBlock` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PullBlock` | 150 | 159 | 10 | inferred_complete_timeline |
| `Action_None` | 160 | 239 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_BallSnap` | 74 | 84 | 11 | inferred_complete_timeline |
| `Action_DownBlock` | 85 | 122 | 38 | inferred_complete_timeline |
| `Action_DownBlock` | 128 | 130 | 3 | inferred_complete_timeline |
| `Action_DownBlock` | 133 | 151 | 19 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 182 | 192 | 11 | inferred_complete_timeline |
| `Action_None` | 196 | 239 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 134 | 138 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_DownBlock` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_None` | 160 | 199 | 40 | inferred_complete_timeline |
| `Action_None` | 204 | 239 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 113 | 40 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 118 | 45 | inferred_complete_timeline |
| `Action_None` | 121 | 180 | 60 | inferred_complete_timeline |
| `Action_None` | 182 | 187 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 239 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–125
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_DownBlock` | 75 | 87 | 13 | inferred_complete_timeline |
| `Action_DownBlock` | 90 | 125 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 88 | 15 | inferred_complete_timeline |
| `Action_None` | 90 | 91 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 166 | 69 | inferred_complete_timeline |
| `Action_None` | 182 | 239 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–217
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 190 | 117 | inferred_complete_timeline |
| `Action_None` | 213 | 217 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 221 | 148 | inferred_complete_timeline |
| `Action_None` | 224 | 239 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 173 | 100 | inferred_complete_timeline |
| `Action_None` | 178 | 205 | 28 | inferred_complete_timeline |
| `Action_None` | 226 | 228 | 3 | inferred_complete_timeline |
| `Action_None` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 123 | 50 | inferred_complete_timeline |
| `Action_None` | 136 | 147 | 12 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 222 | 149 | inferred_complete_timeline |
| `Action_None` | 227 | 237 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 73 | 74 | inferred_complete_timeline |
| `Action_None` | 74 | 239 | 166 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 4–11 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 43–45 | 3 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 124–126 | 3 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 140–239 | 100 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 143–239 | 77 | 7 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 147–205 | 50 | 3 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 207–239 | 33 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 239–239 | 1 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (4 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `7` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [74–84], lower_priority='Action_DownBlock' annotated_start=75, effective_Action_DownBlock_start=85.
- ⚠️ Action 'Action_None' range [74-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-215] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-221] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-160] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-175] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-117] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-222] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-237] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [85-122] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [128-130] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [133-151] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-190] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-217] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-173] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-205] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-228] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-87] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [134-138] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-141] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [75-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [90-151] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-194] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-211] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-221] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [75-88] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [94-137] for track '15' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [142-143] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-123] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-147] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-118] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-180] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-113] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [75-87] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [90-125] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-91] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-166] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-239] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [27-59] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-79] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-218] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-237] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-11] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-45] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-239] for track '25' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-160] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-179] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-205] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-239] for track '29' has 1 frames without a visible bounding box.
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

</details>