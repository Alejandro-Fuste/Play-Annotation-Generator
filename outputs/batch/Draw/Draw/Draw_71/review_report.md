# Play-Annotation-Generator Annotation Review — Draw_71

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_71`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 83
- **Validation Warnings:** 63
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 4
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `10` | `9` |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | offense | `13` | `12` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `16` |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | offense | `17` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `17` | `16` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `10` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `16` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `2` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 74 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 71 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 72 | START | 72 | 86 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `10` | `9` | 75 | START | 75 | 103 |
| ❌ MISSING SEGMENT | `Action_PassBlock` | C | `13` | `12` | 75 | START | N/A | N/A |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `19` | 75 | START | 75 | 156 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `5` | 75 | START | 75 | 124 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `16` | 88 | END | 72 | 88 |
| ✅ EXACT | `Action_FakePassDroptoHandoff` | QB | `17` | `16` | 93 | START | 93 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `17` | `16` | 111 | START | 111 | 128 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 156 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–226
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_SnapReceive` | 72 | 88 | 17 | inferred_complete_timeline |
| `Action_None` | 89 | 92 | 4 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 93 | 110 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 111 | 128 | 18 | inferred_complete_timeline |
| `Action_BallCarry` | 133 | 226 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 110 | 39 | inferred_complete_timeline |
| `Action_None` | 118 | 135 | 18 | inferred_complete_timeline |
| `Action_None` | 138 | 142 | 5 | inferred_complete_timeline |
| `Action_None` | 145 | 147 | 3 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 166 | 167 | 2 | inferred_complete_timeline |
| `Action_None` | 169 | 239 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 109 | 38 | inferred_complete_timeline |
| `Action_None` | 117 | 118 | 2 | inferred_complete_timeline |
| `Action_None` | 120 | 139 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 124 | 50 | inferred_complete_timeline |
| `Action_PassBlock` | 126 | 128 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 156 | 26 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 156 | 82 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–86
- **Visible Samples:** 87

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_BallSnap` | 72 | 86 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 74 | 75 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 103 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 156 | 38 | inferred_complete_timeline |
| `Action_None` | 157 | 239 | 83 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–138
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 85 | 14 | inferred_complete_timeline |
| `Action_None` | 91 | 138 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 110 | 39 | inferred_complete_timeline |
| `Action_None` | 115 | 126 | 12 | inferred_complete_timeline |
| `Action_None` | 128 | 239 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 239 | 168 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_None` | 72 | 238 | 167 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 24–239 | 203 | 4 | Undefined position; Undefined team |
| `21` | `24` | Position_Unknown | Team_Unknown | 109–119 | 9 | 2 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 112–239 | 125 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 135–235 | 85 | 5 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 143–178 | 28 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 166–169 | 4 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 180–239 | 59 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 187–188 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 225–239 | 12 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `10` (2 segments found)
- ❌ Missing segment for action `Action_PassBlock` on target `13` (C)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `17` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `3`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `8` (actor_track_id `9`): `SAF1` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [72–86], lower_priority='Action_PassBlock' annotated_start=75, effective_Action_PassBlock_start=87.
- ⚠️ Action 'Action_None' range [72-238] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [126-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-109] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [117-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-139] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-103] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [72-86] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-110] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-142] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-147] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-239] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [111-128] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [133-226] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-126] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-92] for track '20' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-110] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-121] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-143] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-152] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-169] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-235] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-167] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-178] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-169] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '29' has 1 frames without a visible bounding box.
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

</details>