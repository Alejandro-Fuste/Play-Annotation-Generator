# Play-Annotation-Generator Annotation Review — SlantAndGo_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SlantAndGo_31`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_SlantAndGo`
- **Result:** `Result_Rec`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 5
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SellRoute` | WR1 | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | offense | `5` | `5` |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `4` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `5` | `Group` | 0 | START | 0 | 63 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 41 | START | 41 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `10` | 49 | START | 49 | 63 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 49 | START | 57 | 123 |
| ✅ EXACT | `Action_PassBlock` | LT | `15` | `15` | 49 | START | 49 | 52 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 49 | START | 49 | 131 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 56 | END | 41 | 56 |
| ✅ EXACT | `Action_SellRoute` | WR1 | `5` | `5` | 64 | START | 64 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_VerticalStem` | WR1 | `5` | `5` | 98 | START | 98 | 102 |
| ❌ MISSING SEGMENT | `Action_ThrowPass` | QB | `17` | `17` | 125 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_None` | 57 | 114 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–46
- **Visible Samples:** 47

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 46 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 63 | 64 | inferred_complete_timeline |
| `Action_SellRoute` | 64 | 95 | 32 | inferred_complete_timeline |
| `Action_VerticalStem` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_VerticalStem` | 104 | 117 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–39
- **Visible Samples:** 40

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 154 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 122 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–52
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 13 | 36 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 52 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 56 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 123 | 67 | inferred_complete_timeline |
| `Action_PassBlock` | 127 | 155 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 159 | 210 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–131
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 22 | 48 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 131 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–83
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 63 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 82 | 83 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 44 | 4 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_None` | 50 | 53 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 66 | 26 | inferred_complete_timeline |
| `Action_None` | 69 | 71 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–110
- **Visible Samples:** 99

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 71 | 31 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 96 | 13 | inferred_complete_timeline |
| `Action_None` | 99 | 110 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 53 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–74
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 50 | 10 | inferred_complete_timeline |
| `Action_None` | 53 | 74 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 210 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 149 | 109 | inferred_complete_timeline |
| `Action_None` | 151 | 153 | 3 | inferred_complete_timeline |
| `Action_None` | 155 | 159 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 210 | 170 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 90 | 50 | inferred_complete_timeline |
| `Action_None` | 94 | 97 | 4 | inferred_complete_timeline |
| `Action_None` | 101 | 188 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–132
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 25 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 29 | 40 | 12 | inferred_complete_timeline |
| `Action_None` | 41 | 101 | 61 | inferred_complete_timeline |
| `Action_None` | 109 | 110 | 2 | inferred_complete_timeline |
| `Action_None` | 118 | 121 | 4 | inferred_complete_timeline |
| `Action_None` | 123 | 132 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 155 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 124 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 35–138 | 97 | 3 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 67–210 | 140 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 82–127 | 26 | 3 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 88–147 | 59 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 89–101 | 11 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 92–100 | 6 | 2 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 98–120 | 23 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 103–210 | 107 | 2 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 125–127 | 3 | 1 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 192–210 | 18 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (3 segments found)
- ⚠️ Ambiguous match for action `Action_VerticalStem` and target `5` (2 segments found)
- ❌ Missing segment for action `Action_ThrowPass` on target `17` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `16` (actor_track_id `16`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 70 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 44: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [41–56], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=57.
- ⚠️ Segment 'Action_ThrowPass' for track '17' has invalid range: start=125, end=114. Clamping end to start.
- ⚠️ Action 'Action_None' range [41-154] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-39] for track '1' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '2' starts at frame 41, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [41-44] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-47] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-71] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SellRoute' range [64-95] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [98-102] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_VerticalStem' range [104-117] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-149] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-153] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-159] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-90] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-97] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-188] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-71] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-96] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-110] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [82-83] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-210] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-53] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '13' starts at frame 41, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [41-50] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-74] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-123] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [127-155] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [159-210] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-36] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-52] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-114] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-29] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-124] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-46] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-25] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-101] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-121] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-132] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-18] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-131] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '22' starts at frame 41, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [41-50] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-138] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-79] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [82-100] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-127] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-98] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-94] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-101] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-94] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-100] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-120] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-109] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-127] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-202] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '31' has 1 frames without a visible bounding box.
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