# Play-Annotation-Generator Annotation Review — Draw_19

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_19`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Slide`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 86
- **Validation Warnings:** 61
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 60
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `18` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `5` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `22` | `21` |
| ✅ EXACT | `Action_BallCarry` | QB | offense | `22` | `21` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `17` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `22` | `Group` | 0 | START | 0 | 59 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `5` | `Group` | 0 | START | 0 | 62 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `8` | `Group` | 0 | START | 0 | 59 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 60 | START | 60 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `18` | `17` | 63 | START | 63 | 95 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `18` | 63 | START | 63 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `19` | 63 | START | 63 | 94 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 63 | START | 73 | 92 |
| ✅ EXACT | `Action_PassBlock` | LT | `5` | `4` | 63 | START | 63 | 130 |
| ✅ EXACT | `Action_SnapReceive` | QB | `22` | `21` | 72 | END | 60 | 72 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `22` | `21` | 77 | START | 77 | 100 |
| ✅ EXACT | `Action_BallCarry` | QB | `22` | `21` | 101 | START | 101 | 236 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 130 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_SnapReceive` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_None` | 73 | 76 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 77 | 100 | 24 | inferred_complete_timeline |
| `Action_BallCarry` | 101 | 236 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–123
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 104 | 45 | inferred_complete_timeline |
| `Action_None` | 121 | 123 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 119 | 60 | inferred_complete_timeline |
| `Action_None` | 122 | 239 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 130 | 68 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–104
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 94 | 32 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 104 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_BallSnap` | 60 | 72 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 73 | 92 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 130 | 37 | inferred_complete_timeline |
| `Action_None` | 131 | 142 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 95 | 33 | inferred_complete_timeline |
| `Action_PassBlock` | 98 | 130 | 33 | inferred_complete_timeline |
| `Action_None` | 131 | 239 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 62 | 63 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 130 | 68 | inferred_complete_timeline |
| `Action_None` | 131 | 178 | 48 | inferred_complete_timeline |
| `Action_None` | 185 | 190 | 6 | inferred_complete_timeline |
| `Action_None` | 192 | 239 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 155 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 98 | 39 | inferred_complete_timeline |
| `Action_None` | 100 | 104 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 102 | 43 | inferred_complete_timeline |
| `Action_None` | 106 | 111 | 6 | inferred_complete_timeline |
| `Action_None` | 115 | 119 | 5 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 90 | 31 | inferred_complete_timeline |
| `Action_None` | 92 | 111 | 20 | inferred_complete_timeline |
| `Action_None` | 115 | 239 | 125 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 228 | 169 | inferred_complete_timeline |
| `Action_None` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 236 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 59 | 60 | inferred_complete_timeline |
| `Action_None` | 60 | 239 | 180 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 0–239 | 156 | 6 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 63–81 | 15 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 92–95 | 4 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 106–239 | 134 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 114–239 | 126 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 120–123 | 4 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 134–239 | 96 | 4 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 164–173 | 10 | 1 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 191–238 | 48 | 1 | Undefined position; Undefined team |
| `31` | `46` | Position_Unknown | Team_Unknown | 208–216 | 9 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 39 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [60–72], lower_priority='Action_PassBlock' annotated_start=63, effective_Action_PassBlock_start=73.
- ⚠️ Action 'Action_None' range [60-155] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-90] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-111] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-98] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-104] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-119] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-104] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-123] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-102] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-228] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-95] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [98-130] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-178] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-94] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [73-92] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [101-236] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [4-46] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-84] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-152] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-73] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-95] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-165] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-173] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-238] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-216] for track '31' has 2 frames without a visible bounding box.
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