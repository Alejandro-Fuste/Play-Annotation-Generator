# Play-Annotation-Generator Annotation Review — Counter_107

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_107`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 85
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 79
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `22` | `21` |
| ✅ EXACT | `Action_DownBlock` | RG | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | offense | `17` | `16` |
| ✅ EXACT | `Action_PullLeadBlock` | SAF1 | defense | `13` | `12` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `20` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `22` | `Group` | 0 | START | 0 | 13 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 13 |
| ✅ EXACT | `Action_BallSnap` | C | `22` | `21` | 14 | START | 14 | 29 |
| ✅ EXACT | `Action_DownBlock` | RG | `21` | `20` | 18 | START | 18 | 22 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | LG | `17` | `16` | 18 | START | 18 | 65 |
| ✅ EXACT | `Action_PullLeadBlock` | SAF1 | `13` | `12` | 18 | START | 18 | 120 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | C | `22` | `21` | 29 | END | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | C | `22` | `21` | 56 | START | 56 | 68 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 120 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 87 | 74 | inferred_complete_timeline |
| `Action_None` | 89 | 155 | 67 | inferred_complete_timeline |
| `Action_None` | 158 | 215 | 58 | inferred_complete_timeline |
| `Action_None` | 220 | 239 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 226 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 204 | 191 | inferred_complete_timeline |
| `Action_None` | 206 | 239 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 129 | 116 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 239 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–93
- **Visible Samples:** 93

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 81 | 68 | inferred_complete_timeline |
| `Action_None` | 83 | 93 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PullBlock` | 18 | 65 | 48 | inferred_complete_timeline |
| `Action_PullBlock` | 67 | 120 | 54 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_BallSnap` | 14 | 29 | 16 | inferred_complete_timeline |
| `Action_None` | 30 | 55 | 26 | inferred_complete_timeline |
| `Action_BallCarry` | 56 | 68 | 13 | inferred_complete_timeline |
| `Action_BallCarry` | 71 | 239 | 169 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_DownBlock` | 18 | 22 | 5 | inferred_complete_timeline |
| `Action_None` | 23 | 32 | 10 | inferred_complete_timeline |
| `Action_None` | 58 | 71 | 14 | inferred_complete_timeline |
| `Action_None` | 77 | 82 | 6 | inferred_complete_timeline |
| `Action_None` | 93 | 99 | 7 | inferred_complete_timeline |
| `Action_None` | 104 | 239 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–43
- **Visible Samples:** 44

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 43 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 206 | 193 | inferred_complete_timeline |
| `Action_None` | 210 | 216 | 7 | inferred_complete_timeline |
| `Action_None` | 218 | 219 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–129
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 123 | 110 | inferred_complete_timeline |
| `Action_None` | 128 | 129 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 83 | 70 | inferred_complete_timeline |
| `Action_None` | 93 | 103 | 11 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 86 | 73 | inferred_complete_timeline |
| `Action_None` | 90 | 125 | 36 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 159 | 16 | inferred_complete_timeline |
| `Action_None` | 164 | 210 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 71 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 133

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 132 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 18 | 120 | 103 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_None` | 14 | 239 | 226 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–239 | 240 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 40–137 | 13 | 5 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 51–239 | 177 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 97–142 | 46 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 99–239 | 141 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 125–239 | 110 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 129–150 | 16 | 3 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 145–239 | 95 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 149–193 | 38 | 4 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 154–238 | 66 | 5 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 235–239 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PullBlock` and target `17` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `22` (C)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `22` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 59 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 216: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '16' (LG) duration 103 frames exceeds threshold 90 frames [start=18, end=120].
- ⚠️ Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [14–29], lower_priority='Action_SnapReceive' annotated_start=14, effective_Action_SnapReceive_start=30.
- ⚠️ Action 'Action_None' range [14-129] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-239] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-204] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-239] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-125] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-159] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-83] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-103] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-43] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-123] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-206] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-219] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-93] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [18-65] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-155] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-215] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [14-226] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-32] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-99] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '21' starts at frame 30, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [30-55] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [56-68] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-41] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-70] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-114] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-121] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-142] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-137] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-141] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-161] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-185] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-193] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-165] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-202] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-238] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-239] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
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

</details>