# Play-Annotation-Generator Annotation Review — CrackToss_80

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `CrackToss_80`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_CrackToss`
- **Result:** `Result_Touchdown`
- **Result Frame:** 239
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 95
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `24` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | LT | offense | `22` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE3 | offense | `24` | `23` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `13` |
| ✅ EXACT | `Action_Toss` | QB | offense | `14` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `9` | `8` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `1` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `22` | `Group` | 0 | START | 2 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `24` | `Group` | 0 | START | 12 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `5` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `7` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `9` | `Group` | 0 | START | 0 | 16 |
| ✅ EXACT | `Action_BallSnap` | LT | `22` | `21` | 59 | START | 59 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_CrackBlock` | TE3 | `24` | `23` | 62 | START | 62 | 83 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | C | `5` | `4` | 62 | START | 62 | 128 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `13` | 66 | END | 59 | 66 |
| ✅ EXACT | `Action_Toss` | QB | `14` | `13` | 69 | START | 69 | 87 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `9` | `8` | 88 | START | 88 | 144 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 144 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |
| `Action_Toss` | 69 | 87 | 19 | inferred_complete_timeline |
| `Action_None` | 88 | 150 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_PreSnap` | 20 | 87 | 68 | inferred_complete_timeline |
| `Action_BallCarry` | 88 | 144 | 57 | inferred_complete_timeline |
| `Action_BallCarry` | 146 | 148 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 117 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 94 | 36 | inferred_complete_timeline |
| `Action_None` | 100 | 150 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 73 | 15 | inferred_complete_timeline |
| `Action_None` | 77 | 150 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `24`</summary>

- **xml_track_id:** `23`
- **actor_track_id:** `24`
- **team_side:** `offense`
- **Visible Frames:** 12–150
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 12 | 61 | 50 | inferred_complete_timeline |
| `Action_CrackBlock` | 62 | 83 | 22 | inferred_complete_timeline |
| `Action_CrackBlock` | 88 | 96 | 9 | inferred_complete_timeline |
| `Action_CrackBlock` | 102 | 144 | 43 | inferred_complete_timeline |
| `Action_None` | 145 | 150 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 2–80
- **Visible Samples:** 79

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 2 | 58 | 57 | inferred_complete_timeline |
| `Action_BallSnap` | 59 | 66 | 8 | inferred_complete_timeline |
| `Action_None` | 67 | 80 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 75 | 17 | inferred_complete_timeline |
| `Action_None` | 80 | 150 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PullBlock` | 62 | 128 | 67 | inferred_complete_timeline |
| `Action_PullBlock` | 130 | 137 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–89
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 83 | 25 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 138

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 120 | 62 | inferred_complete_timeline |
| `Action_None` | 124 | 135 | 12 | inferred_complete_timeline |
| `Action_None` | 140 | 141 | 2 | inferred_complete_timeline |
| `Action_None` | 143 | 145 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–135
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 117 | 59 | inferred_complete_timeline |
| `Action_None` | 131 | 135 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 131 | 73 | inferred_complete_timeline |
| `Action_None` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_None` | 139 | 150 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 10 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 30 | 58 | 29 | inferred_complete_timeline |
| `Action_None` | 59 | 94 | 36 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |
| `Action_None` | 119 | 120 | 2 | inferred_complete_timeline |
| `Action_None` | 123 | 137 | 15 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |
| `Action_None` | 144 | 145 | 2 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–130
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 107 | 49 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |
| `Action_None` | 127 | 130 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 150 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_None` | 59 | 139 | 81 | inferred_complete_timeline |
| `Action_None` | 144 | 149 | 6 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `2` | `3` | Position_Unknown | Team_Unknown | 0–150 | 151 | 2 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 0–2 | 3 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 7–72 | 46 | 6 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 34–35 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 82–108 | 25 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 86–131 | 39 | 4 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 111–150 | 39 | 2 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 112–117 | 6 | 1 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 124–150 | 25 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 125–150 | 26 | 1 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 126–135 | 10 | 1 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 145–150 | 6 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_CrackBlock` and target `24` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `9` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `3` (actor_track_id `4`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 70 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [59-117] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-139] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-149] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [62-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [130-137] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-83] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-94] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-150] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-75] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-150] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-16] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [88-144] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [146-148] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-107] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-130] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-131] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-136] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-150] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-150] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-117] for track '15' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-2] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-120] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-135] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-141] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-145] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-10] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-94] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-137] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-145] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-73] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-150] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-150] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-80] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [7-35] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [38-40] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-50] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-67] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [62-83] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_CrackBlock' range [88-96] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-103] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-108] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-127] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-131] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-114] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-126] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [129-150] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-150] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-135] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-150] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Player track '2' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '2' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
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

</details>