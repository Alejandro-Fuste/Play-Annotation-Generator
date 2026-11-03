# Play-Annotation-Generator Annotation Review — OutRoutes_21

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_21`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 41
- **Ball Tracks:** 0
- **Action Segments:** 99
- **Validation Warnings:** 112
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 77
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `8` | `8` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `4` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 9 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `14` | `14` | 10 | START | 10 | 32 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `17` | `17` | 10 | START | 10 | 33 |
| ✅ EXACT | `Action_PassBlock` | LT | `18` | `18` | 10 | START | 10 | 239 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 10 | START | 10 | 239 |
| ✅ EXACT | `Action_PassBlock` | RT | `8` | `8` | 10 | START | 10 | 72 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `3` | `3` | 19 | START | 19 | 75 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 19 | END | 19 | 19 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 45 | START | 45 | 56 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `3` | `3` | 76 | START | 76 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `3` | `3` | 85 | START | 85 | 92 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_SnapReceive` | 19 | 19 | 1 | inferred_complete_timeline |
| `Action_None` | 20 | 44 | 25 | inferred_complete_timeline |
| `Action_ThrowPass` | 45 | 56 | 12 | inferred_complete_timeline |
| `Action_None` | 57 | 239 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 239 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunOutRoute` | 19 | 75 | 57 | inferred_complete_timeline |
| `Action_SecureCatch` | 76 | 84 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 85 | 92 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 94 | 114 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 117 | 119 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 33 | 24 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 239 | 202 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 32 | 23 | inferred_complete_timeline |
| `Action_PassBlock` | 94 | 239 | 146 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 239 | 230 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 72 | 63 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–92
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 66 | 67 | inferred_complete_timeline |
| `Action_PreSnap` | 69 | 92 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 42 | 239 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 196 | 198 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 205 | 207 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 215 | 225 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 233 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 105 | 106 | inferred_complete_timeline |
| `Action_PreSnap` | 107 | 115 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 127 | 11 | inferred_complete_timeline |
| `Action_PreSnap` | 129 | 239 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–126
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 202 | 203 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 239

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 48 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 50 | 239 | 190 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–119 | 96 | 6 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 30–239 | 210 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 70–239 | 170 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 75–76 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 98–239 | 99 | 10 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 118–119 | 2 | 1 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 143–150 | 6 | 2 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 154–156 | 3 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 163–224 | 46 | 3 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 176–201 | 15 | 3 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 177–182 | 5 | 2 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 181–201 | 20 | 2 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 183–184 | 2 | 1 | Undefined position; Undefined team |
| `36` | `48` | Position_Unknown | Team_Unknown | 191–192 | 2 | 1 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 202–239 | 31 | 6 | Undefined position; Undefined team |
| `38` | `52` | Position_Unknown | Team_Unknown | 224–239 | 11 | 3 | Undefined position; Undefined team |
| `39` | `54` | Position_Unknown | Team_Unknown | 231–235 | 5 | 1 | Undefined position; Undefined team |
| `40` | `55` | Position_Unknown | Team_Unknown | 233–235 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 72 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [85-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [94-114] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [117-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-126] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-202] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-72] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-48] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-105] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-115] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-127] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-32] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [94-239] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-33] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [196-198] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [215-225] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-233] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-66] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [39-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-66] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-77] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-119] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-103] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-106] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-125] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-132] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-149] for track '26' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-153] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-167] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-174] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-211] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [143-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [147-150] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-156] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-215] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-224] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-184] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-182] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [181-196] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [198-201] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-184] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-192] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [202-203] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-207] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [210-211] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [213-221] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-239] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-225] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [229-230] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-239] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-235] for track '39' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '40' has 1 frames without a visible bounding box.
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
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.

</details>