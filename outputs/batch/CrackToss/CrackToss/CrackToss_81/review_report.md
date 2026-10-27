# Play-Annotation-Generator Annotation Review — CrackToss_81

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_81`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 123
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 5
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 82
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `29` | `27` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | RT | offense | `15` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `27` | `26` |
| ✅ EXACT | `Action_PullBlock` | TE1 | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_Toss` | QB | offense | `2` | `1` |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `26` | `25` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 7 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 7 | START | 7 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 7 | START | 7 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `16` | `Group` | 7 | START | 7 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 7 | START | 7 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 7 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `4` | `Group` | 7 | START | 0 | 32 |
| ✅ EXACT | `Action_BallSnap` | Position_Unknown | `29` | `27` | 30 | START | 30 | 37 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | RT | `15` | `14` | 33 | START | 33 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `27` | `26` | 33 | START | 33 | 54 |
| ✅ EXACT | `Action_PullBlock` | TE1 | `4` | `3` | 33 | START | 33 | 114 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `1` | 37 | END | 30 | 37 |
| ✅ EXACT | `Action_Toss` | QB | `2` | `1` | 42 | START | 42 | 59 |
| ✅ EXACT | `Action_BallCarry` | Position_Unknown | `26` | `25` | 60 | START | 60 | 122 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 114 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_SnapReceive` | 30 | 37 | 8 | inferred_complete_timeline |
| `Action_None` | 38 | 41 | 4 | inferred_complete_timeline |
| `Action_Toss` | 42 | 59 | 18 | inferred_complete_timeline |
| `Action_None` | 60 | 85 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_None` | 30 | 73 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–125
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 33 | 114 | 82 | inferred_complete_timeline |
| `Action_None` | 115 | 125 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 7–125
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 100 | 71 | inferred_complete_timeline |
| `Action_None` | 111 | 125 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 7–125
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 125 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 7–18
- **Visible Samples:** 12

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 18 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 7–83
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 32 | 26 | inferred_complete_timeline |
| `Action_CrackBlock` | 33 | 46 | 14 | inferred_complete_timeline |
| `Action_CrackBlock` | 50 | 83 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–6
- **Visible Samples:** 7

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 7–125
- **Visible Samples:** 78

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 50 | 21 | inferred_complete_timeline |
| `Action_None` | 56 | 65 | 10 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_None` | 114 | 116 | 3 | inferred_complete_timeline |
| `Action_None` | 118 | 125 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `23`</summary>

- **xml_track_id:** `22`
- **actor_track_id:** `23`
- **team_side:** `defense`
- **Visible Frames:** 7–85
- **Visible Samples:** 37

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 9 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 12 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 27 | 13 | inferred_complete_timeline |
| `Action_None` | 31 | 43 | 13 | inferred_complete_timeline |
| `Action_None` | 80 | 85 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 7–95
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 63 | 34 | inferred_complete_timeline |
| `Action_None` | 69 | 87 | 19 | inferred_complete_timeline |
| `Action_None` | 89 | 95 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 7–125
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 102 | 73 | inferred_complete_timeline |
| `Action_None` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_None` | 110 | 111 | 2 | inferred_complete_timeline |
| `Action_None` | 115 | 116 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 125 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 7–125
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 57 | 28 | inferred_complete_timeline |
| `Action_None` | 59 | 115 | 57 | inferred_complete_timeline |
| `Action_None` | 120 | 125 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `25`</summary>

- **xml_track_id:** `24`
- **actor_track_id:** `25`
- **team_side:** `defense`
- **Visible Frames:** 7–70
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 70 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 7–76
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 7 | 29 | 23 | inferred_complete_timeline |
| `Action_None` | 30 | 76 | 47 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–125 | 105 | 4 | Undefined position; Undefined team |
| `4` | `5` | Position_Unknown | Team_Unknown | 0–125 | 36 | 2 | Undefined position; Undefined team |
| `5` | `6` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `6` | `7` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `7` | `8` | Position_Unknown | Team_Unknown | 0–78 | 79 | 2 | Undefined position; Undefined team |
| `8` | `9` | Position_Unknown | Team_Unknown | 0–92 | 13 | 3 | Undefined position; Undefined team |
| `9` | `10` | Position_Unknown | Team_Unknown | 0–6 | 7 | 1 | Undefined position; Undefined team |
| `11` | `12` | Position_Unknown | Team_Unknown | 0–1 | 2 | 1 | Undefined position; Undefined team |
| `13` | `14` | Position_Unknown | Team_Unknown | 7–94 | 78 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 7–47 | 38 | 3 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 10–122 | 113 | 2 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 16–120 | 95 | 6 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 24–43 | 19 | 4 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 41–125 | 85 | 1 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 60–95 | 25 | 4 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 64–125 | 21 | 4 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 72–125 | 54 | 1 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 81–125 | 42 | 2 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 99–125 | 20 | 3 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 99–125 | 27 | 1 | Undefined position; Undefined team |
| `35` | `42` | Position_Unknown | Team_Unknown | 122–125 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `27` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `20` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 21 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 21 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 42 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 164: Duplicate assignment for track ID '21' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [30-73] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-85] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-63] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-108] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-125] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-125] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-78] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-92] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-6] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-125] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-74] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-94] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [33-46] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [50-83] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-100] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-125] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-18] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-102] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-107] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-111] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-125] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-63] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-87] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-95] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-65] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-110] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-76] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-57] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-115] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-9] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-12] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [15-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-42] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-70] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [60-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [33-54] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [60-84] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [88-114] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '26' starts at frame 115, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [115-115] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-29] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '27' starts at frame 38, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [38-38] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-43] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-125] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-70] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-95] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-70] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-103] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-118] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-125] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-125] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-92] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-125] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-111] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-116] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-125] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-125] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '4' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '4' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '5' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '5' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '7' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '7' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '8' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '8' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
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