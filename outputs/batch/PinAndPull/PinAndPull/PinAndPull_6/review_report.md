# Play-Annotation-Generator Annotation Review — PinAndPull_6

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `PinAndPull_6`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_PinAndPull`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 100
- **Validation Warnings:** 119
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 16
- **Exact Matches:** 3
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | Team_Unknown | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | offense | `3` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `9` | `8` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `13` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `14` | `Group` | 0 | START | 0 | 4 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 0 | START | 0 | 24 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 24 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 25 | START | 25 | 36 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 28 | START | 28 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | Position_Unknown | `16` | `15` | 28 | START | 28 | 44 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LT | `3` | `2` | 28 | START | 28 | 37 |
| ✅ EXACT | `Action_SnapReceive` | QB | `9` | `8` | 36 | END | 25 | 36 |
| ✅ EXACT | `Action_BallCarry` | QB | `9` | `8` | 48 | START | 48 | 48 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 100 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–48
- **Visible Samples:** 49

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_SnapReceive` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 47 | 11 | inferred_complete_timeline |
| `Action_BallCarry` | 48 | 48 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 61

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 31 | 7 | inferred_complete_timeline |
| `Action_None` | 46 | 50 | 5 | inferred_complete_timeline |
| `Action_None` | 53 | 59 | 7 | inferred_complete_timeline |
| `Action_None` | 124 | 128 | 5 | inferred_complete_timeline |
| `Action_None` | 130 | 132 | 3 | inferred_complete_timeline |
| `Action_None` | 135 | 143 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_None` | 83 | 123 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 28 | 37 | 10 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–80
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_DownBlock` | 28 | 32 | 5 | inferred_complete_timeline |
| `Action_DownBlock` | 43 | 51 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 53 | 80 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–118
- **Visible Samples:** 112

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_BallSnap` | 25 | 36 | 12 | inferred_complete_timeline |
| `Action_None` | 37 | 46 | 10 | inferred_complete_timeline |
| `Action_None` | 50 | 73 | 24 | inferred_complete_timeline |
| `Action_None` | 75 | 80 | 6 | inferred_complete_timeline |
| `Action_None` | 83 | 88 | 6 | inferred_complete_timeline |
| `Action_None` | 90 | 118 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–92
- **Visible Samples:** 26

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_None` | 51 | 56 | 6 | inferred_complete_timeline |
| `Action_None` | 78 | 92 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 131

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_None` | 46 | 53 | 8 | inferred_complete_timeline |
| `Action_None` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_None` | 69 | 127 | 59 | inferred_complete_timeline |
| `Action_None` | 129 | 130 | 2 | inferred_complete_timeline |
| `Action_None` | 138 | 148 | 11 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 25 | 59 | 35 | inferred_complete_timeline |
| `Action_None` | 62 | 103 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 85 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 43 | 19 | inferred_complete_timeline |
| `Action_None` | 46 | 73 | 28 | inferred_complete_timeline |
| `Action_None` | 80 | 82 | 3 | inferred_complete_timeline |
| `Action_None` | 85 | 111 | 27 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 124 | 136 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 25 | 1 | inferred_complete_timeline |
| `Action_None` | 67 | 123 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–109
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 68 | 44 | inferred_complete_timeline |
| `Action_None` | 74 | 78 | 5 | inferred_complete_timeline |
| `Action_None` | 84 | 98 | 15 | inferred_complete_timeline |
| `Action_None` | 101 | 109 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–123
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 116 | 92 | inferred_complete_timeline |
| `Action_None` | 119 | 123 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–127
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 24 | 25 | inferred_complete_timeline |
| `Action_None` | 25 | 127 | 103 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `16` | Position_Unknown | Team_Unknown | 19–131 | 33 | 5 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 26–148 | 120 | 3 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 33–127 | 82 | 4 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 39–53 | 15 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 47–150 | 80 | 6 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 56–95 | 40 | 1 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 60–61 | 2 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 62–75 | 14 | 1 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 66–73 | 8 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 84–138 | 43 | 4 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 90–121 | 32 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 94–101 | 7 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 114–133 | 10 | 4 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 119–122 | 4 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 126–128 | 3 | 1 | Undefined position; Undefined team |
| `30` | `41` | Position_Unknown | Team_Unknown | 127–130 | 4 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `3` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `1`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `1` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 85 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 14: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [25-116] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-123] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-127] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [28-37] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [43-44] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '3' starts at frame 25, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [25-25] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-123] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-85] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-78] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-109] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-43] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-53] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-65] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-130] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-148] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [28-32] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [43-51] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [53-80] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' for track '8' starts at frame 48, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BallCarry' range [48-48] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-59] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-103] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-46] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-73] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-80] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-118] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-31] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-50] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-59] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-132] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-43] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-123] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-56] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-92] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-43] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-73] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-82] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-136] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [28-44] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [48-50] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-125] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-129] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-148] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [33-36] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-105] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-127] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-53] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-118] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-132] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-75] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-123] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-121] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-96] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-133] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-122] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-128] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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

</details>