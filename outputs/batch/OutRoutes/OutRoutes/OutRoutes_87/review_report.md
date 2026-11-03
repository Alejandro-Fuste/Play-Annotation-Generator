# Play-Annotation-Generator Annotation Review — OutRoutes_87

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_87`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 58
- **Validation Warnings:** 56
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 35
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `6` | `6` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `0` | `0` |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `2` | `2` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 57 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 96 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `17` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 16 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `3` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `6` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `9` | `Group` | 0 | START | 0 | 11 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `17` | `17` | 12 | START | 12 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `20` | `20` | 12 | START | 12 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `21` | `21` | 12 | START | 12 | 39 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `6` | `6` | 12 | START | 12 | 96 |
| ✅ EXACT | `Action_PassBlock` | RT | `9` | `9` | 12 | START | 12 | 97 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `0` | `0` | 17 | START | 17 | 210 |
| ✅ EXACT | `Action_RunOutRoute` | WR1 | `2` | `2` | 17 | START | 17 | 83 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 17 | END | 17 | 17 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 52 | START | 52 | 59 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `2` | `2` | 84 | START | 84 | 91 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `2` | `2` | 92 | START | 92 | 180 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–139
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_SnapReceive` | 17 | 17 | 1 | inferred_complete_timeline |
| `Action_None` | 18 | 51 | 34 | inferred_complete_timeline |
| `Action_ThrowPass` | 52 | 59 | 8 | inferred_complete_timeline |
| `Action_None` | 60 | 76 | 17 | inferred_complete_timeline |
| `Action_None` | 79 | 85 | 7 | inferred_complete_timeline |
| `Action_None` | 88 | 89 | 2 | inferred_complete_timeline |
| `Action_None` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_None` | 97 | 108 | 12 | inferred_complete_timeline |
| `Action_None` | 112 | 120 | 9 | inferred_complete_timeline |
| `Action_None` | 122 | 139 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–96
- **Visible Samples:** 97

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunOutRoute` | 17 | 83 | 67 | inferred_complete_timeline |
| `Action_SecureCatch` | 84 | 91 | 8 | inferred_complete_timeline |
| `Action_BallCarry` | 92 | 180 | 89 | inferred_complete_timeline |
| `Action_BallCarry` | 182 | 210 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 16 | 17 | inferred_complete_timeline |
| `Action_RunOutRoute` | 17 | 210 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 57 | 58 | inferred_complete_timeline |
| `Action_PreSnap` | 63 | 210 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–103
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 96 | 85 | inferred_complete_timeline |
| `Action_PassBlock` | 99 | 103 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 39 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 48 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 51 | 166 | 116 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–71
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 41 | 30 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 71 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 75 | 64 | inferred_complete_timeline |
| `Action_PassBlock` | 91 | 210 | 120 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–97
- **Visible Samples:** 98

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 12 | 97 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 71 | 32 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 75 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 55 | 56 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–202
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 166 | 167 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 202 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 204

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 112 | 113 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 127 | 210 | 84 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 188 | 189 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 172 | 173 | inferred_complete_timeline |
| `Action_PreSnap` | 176 | 210 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 0–7 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 83–142 | 60 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 94–210 | 117 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 123–133 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `2` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF2` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 46 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_RunOutRoute' range [17-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-57] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-210] for track '1' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [92-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [182-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-172] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [176-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [127-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-96] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [99-103] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-97] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-188] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-112] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-166] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [173-202] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-34] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-71] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-75] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ThrowPass' range [52-59] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-85] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-89] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-108] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-120] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-139] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-75] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [91-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-41] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-71] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [12-39] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-48] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [51-166] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-7] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-142] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-210] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [123-133] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>