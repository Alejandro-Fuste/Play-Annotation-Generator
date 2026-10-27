# Play-Annotation-Generator Annotation Review — Counter_141

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_141`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 109
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 2
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 85
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | WR3 | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | RT | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | offense | `18` | `17` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 63 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 69 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 69 |
| ✅ EXACT | `Action_BallSnap` | WR3 | `1` | `0` | 64 | START | 64 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `14` | `13` | 70 | START | 70 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `17` | `16` | 70 | START | 70 | 98 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 70 | START | 70 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `22` | `21` | 70 | START | 70 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `6` | `5` | 70 | START | 70 | 115 |
| ✅ EXACT | `Action_SnapReceive` | RT | `18` | `17` | 78 | END | 64 | 78 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RT | `18` | `17` | 98 | START | 98 | 183 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 170 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–293
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 293 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_BallSnap` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 299 | 221 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 70 | 115 | 46 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 126 | 140 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_DownBlock` | 70 | 92 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 98 | 110 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_DownBlock` | 70 | 98 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 109 | 124 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_DownBlock` | 70 | 83 | 14 | inferred_complete_timeline |
| `Action_DownBlock` | 86 | 87 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 69 | 70 | inferred_complete_timeline |
| `Action_PullBlock` | 70 | 118 | 49 | inferred_complete_timeline |
| `Action_PullBlock` | 120 | 124 | 5 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 167 | 42 | inferred_complete_timeline |
| `Action_PullBlock` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 234 | 64 | inferred_complete_timeline |
| `Action_None` | 236 | 241 | 6 | inferred_complete_timeline |
| `Action_None` | 244 | 250 | 7 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SnapReceive` | 64 | 78 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 97 | 19 | inferred_complete_timeline |
| `Action_BallCarry` | 98 | 183 | 86 | inferred_complete_timeline |
| `Action_BallCarry` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 83 | 20 | inferred_complete_timeline |
| `Action_None` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 105 | 107 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 157 | 94 | inferred_complete_timeline |
| `Action_None` | 165 | 167 | 3 | inferred_complete_timeline |
| `Action_None` | 169 | 202 | 34 | inferred_complete_timeline |
| `Action_None` | 213 | 299 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–297
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 153 | 90 | inferred_complete_timeline |
| `Action_None` | 156 | 157 | 2 | inferred_complete_timeline |
| `Action_None` | 171 | 187 | 17 | inferred_complete_timeline |
| `Action_None` | 191 | 286 | 96 | inferred_complete_timeline |
| `Action_None` | 288 | 297 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 154 | 91 | inferred_complete_timeline |
| `Action_None` | 157 | 171 | 15 | inferred_complete_timeline |
| `Action_None` | 175 | 299 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 298

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 115 | 52 | inferred_complete_timeline |
| `Action_None` | 117 | 198 | 82 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–194
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 191 | 128 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 262 | 199 | inferred_complete_timeline |
| `Action_None` | 264 | 299 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_None` | 64 | 299 | 236 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `14` | `15` | Position_Unknown | Team_Unknown | 0–299 | 296 | 5 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 9–101 | 85 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 104–299 | 184 | 3 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 114–299 | 185 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 122–299 | 170 | 3 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 130–299 | 163 | 4 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 133–134 | 2 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 134–135 | 2 | 1 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 145–202 | 6 | 2 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 155–214 | 59 | 2 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 163–180 | 8 | 2 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 188–198 | 6 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 208–299 | 91 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 210–299 | 90 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 219–221 | 3 | 1 | Undefined position; Undefined team |
| `36` | `42` | Position_Unknown | Team_Unknown | 240–241 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 251–261 | 4 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `22` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `12`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `19`): `SAF1` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 283: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '21' (RG) duration 101 frames exceeds threshold 90 frames [start=70, end=170].
- ⚠️ Action 'Action_None' range [64-115] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [70-115] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [126-140] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-154] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [70-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [98-110] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-187] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-286] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [288-297] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-299] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [70-83] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [86-87] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-94] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-105] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-157] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-202] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [70-98] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [109-124] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [98-183] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [192-299] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-262] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-293] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [70-118] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [120-124] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-167] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-234] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-241] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [9-63] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-138] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-256] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-134] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-148] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-165] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-214] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-198] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-215] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-299] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-241] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-261] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
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