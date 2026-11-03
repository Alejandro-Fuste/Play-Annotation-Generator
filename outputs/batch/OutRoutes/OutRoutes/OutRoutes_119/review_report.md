# Play-Annotation-Generator Annotation Review — OutRoutes_119

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_119`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 70
- **Validation Warnings:** 83
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
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `5` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR4 | offense | `1` | `1` |
| ✅ EXACT | `Action_BallCarry` | WR4 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `0` | `Group` | 0 | START | 0 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 21 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `15` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 17 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 180 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `15` | `15` | 18 | START | 18 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 18 | START | 18 | 23 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `19` | `19` | 18 | START | 18 | 53 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `20` | `20` | 18 | START | 18 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `21` | `21` | 18 | START | 18 | 76 |
| ✅ EXACT | `Action_RunOutRoute` | WR4 | `1` | `1` | 22 | START | 22 | 92 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `5` | `5` | 22 | START | 22 | 180 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 22 | END | 22 | 22 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 59 | START | 59 | 70 |
| ✅ EXACT | `Action_SecureCatch` | WR4 | `1` | `1` | 93 | START | 93 | 101 |
| ✅ EXACT | `Action_BallCarry` | WR4 | `1` | `1` | 102 | START | 102 | 159 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 180

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_SnapReceive` | 22 | 22 | 1 | inferred_complete_timeline |
| `Action_None` | 23 | 58 | 36 | inferred_complete_timeline |
| `Action_ThrowPass` | 59 | 70 | 12 | inferred_complete_timeline |
| `Action_None` | 71 | 142 | 72 | inferred_complete_timeline |
| `Action_None` | 144 | 180 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_RunOutRoute` | 22 | 180 | 159 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 21 | 22 | inferred_complete_timeline |
| `Action_RunOutRoute` | 22 | 92 | 71 | inferred_complete_timeline |
| `Action_SecureCatch` | 93 | 101 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 102 | 159 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–151
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 71

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 64 | 47 | inferred_complete_timeline |
| `Action_PassBlock` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 79 | 82 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 53 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 134 | 72 | inferred_complete_timeline |
| `Action_PassBlock` | 136 | 180 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 23 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 180 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 76 | 59 | inferred_complete_timeline |
| `Action_PassBlock` | 89 | 180 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–180
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 17 | 18 | inferred_complete_timeline |
| `Action_PassBlock` | 18 | 51 | 34 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 95 | 39 | inferred_complete_timeline |
| `Action_PassBlock` | 103 | 180 | 78 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 102 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 104 | 180 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–106
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 96 | 97 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 106 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–68
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_PreSnap` | 66 | 68 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–180
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 180 | 181 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 21–28 | 8 | 1 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 43–59 | 16 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 78–103 | 23 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 81–82 | 2 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 83–87 | 5 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 89–180 | 92 | 1 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 90–180 | 82 | 3 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 91–180 | 90 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 122–126 | 5 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 134–166 | 10 | 3 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 135–178 | 26 | 5 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 158–180 | 23 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 57 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [102-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [22-180] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-106] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-96] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-102] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-180] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-51] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-95] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [103-180] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-23] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-180] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-180] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-53] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [136-180] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-64] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [74-75] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [79-82] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [18-76] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [89-180] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [21-28] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [43-47] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-59] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-92] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-103] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-82] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [83-87] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-93] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-157] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-180] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [122-126] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-136] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [140-144] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [165-166] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [135-144] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [152-154] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-158] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-178] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-180] for track '33' has 3 frames without a visible bounding box.
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

</details>