# Play-Annotation-Generator Annotation Review — Counter_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_29`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 104
- **Validation Warnings:** 107
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `13` |
| ⚠️ START CHANGED | `Action_DownBlock` | C | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | offense | `15` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `8` | `7` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `11` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `15` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `7` | `Group` | 0 | START | 0 | 55 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 67 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `13` | 56 | START | 56 | 60 |
| ⚠️ START CHANGED | `Action_DownBlock` | C | `14` | `13` | 60 | START | 61 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | RT | `16` | `15` | 60 | START | 60 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `12` | `11` | 60 | START | 60 | 60 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | TE | `15` | `14` | 60 | START | 60 | 151 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 60 | END | 56 | 60 |
| ✅ EXACT | `Action_PlaySideFakeStep` | RB | `8` | `7` | 68 | START | 68 | 103 |
| ⚠️ AMBIGUOUS MATCH | `Action_Handoff` | QB | `18` | `17` | 92 | START | 92 | 99 |
| ✅ EXACT | `Action_BallCarry` | RB | `8` | `7` | 104 | START | 104 | 131 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_SnapReceive` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 61 | 91 | 31 | inferred_complete_timeline |
| `Action_Handoff` | 92 | 99 | 8 | inferred_complete_timeline |
| `Action_Handoff` | 101 | 103 | 3 | inferred_complete_timeline |
| `Action_None` | 104 | 210 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PlaySideFakeStep` | 68 | 103 | 36 | inferred_complete_timeline |
| `Action_BallCarry` | 104 | 131 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 134 | 79 | inferred_complete_timeline |
| `Action_None` | 136 | 167 | 32 | inferred_complete_timeline |
| `Action_None` | 172 | 175 | 4 | inferred_complete_timeline |
| `Action_None` | 181 | 186 | 6 | inferred_complete_timeline |
| `Action_None` | 190 | 197 | 8 | inferred_complete_timeline |
| `Action_None` | 201 | 204 | 4 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 103 | 48 | inferred_complete_timeline |
| `Action_None` | 106 | 210 | 105 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 60 | 151 | 92 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 153 | 156 | 4 | inferred_complete_timeline |
| `Action_None` | 157 | 210 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_BallSnap` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 61 | 67 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_PullBlock` | 60 | 60 | 1 | inferred_complete_timeline |
| `Action_PullBlock` | 79 | 81 | 3 | inferred_complete_timeline |
| `Action_PullBlock` | 83 | 94 | 12 | inferred_complete_timeline |
| `Action_PullBlock` | 126 | 153 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 31 | 59 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 60 | 64 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 68 | 108 | 41 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 156 | 21 | inferred_complete_timeline |
| `Action_None` | 157 | 181 | 25 | inferred_complete_timeline |
| `Action_None` | 195 | 201 | 7 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 75

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 26 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 35 | 44 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 55 | 6 | inferred_complete_timeline |
| `Action_None` | 56 | 60 | 5 | inferred_complete_timeline |
| `Action_None` | 108 | 124 | 17 | inferred_complete_timeline |
| `Action_None` | 127 | 134 | 8 | inferred_complete_timeline |
| `Action_None` | 136 | 157 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 70 | 15 | inferred_complete_timeline |
| `Action_None` | 79 | 210 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 67 | 12 | inferred_complete_timeline |
| `Action_None` | 70 | 74 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 17

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 38 | 39 | 2 | inferred_complete_timeline |
| `Action_None` | 58 | 62 | 5 | inferred_complete_timeline |
| `Action_None` | 70 | 75 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–168
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 138 | 83 | inferred_complete_timeline |
| `Action_None` | 140 | 145 | 6 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 168 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 101 | 46 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 113 | 58 | inferred_complete_timeline |
| `Action_None` | 115 | 210 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 210 | 155 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |
| `Action_None` | 56 | 161 | 106 | inferred_complete_timeline |
| `Action_None` | 166 | 190 | 25 | inferred_complete_timeline |
| `Action_None` | 196 | 204 | 9 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `22` | Position_Unknown | Team_Unknown | 51–210 | 104 | 4 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 92–108 | 16 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 93–150 | 55 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 104–210 | 107 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 125–206 | 65 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 141–146 | 6 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 157–210 | 53 | 2 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 163–210 | 34 | 5 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 174–210 | 37 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 197–210 | 8 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_DownBlock` for actor_track_id `14` (C): Annotated start 60 != Inferred start 61
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `12` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_Handoff` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 81 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '11' (RG) duration 94 frames exceeds threshold 90 frames [start=60, end=153].
- ⚠️ Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [56–60], lower_priority='Action_DownBlock' annotated_start=60, effective_Action_DownBlock_start=61.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '15' (RT) duration 97 frames exceeds threshold 90 frames [start=60, end=156].
- ⚠️ Action 'Action_None' range [56-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-161] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-190] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-113] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-138] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-145] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-101] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-134] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-175] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-197] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-204] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PlaySideFakeStep' range [68-103] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [104-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-70] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' for track '11' starts at frame 60, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_PullBlock' range [60-60] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [79-81] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [83-94] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [126-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-67] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-74] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [61-67] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [60-151] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [60-64] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [68-108] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [136-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-181] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-201] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-103] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_Handoff' range [92-99] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-26] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [35-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [50-55] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-60] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-124] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-134] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-157] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-39] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-143] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-129] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-206] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-146] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-204] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-167] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-181] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-189] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-199] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '30' has 1 frames without a visible bounding box.
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

</details>