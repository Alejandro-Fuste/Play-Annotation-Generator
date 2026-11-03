# Play-Annotation-Generator Annotation Review — OutRoutes_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_117`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 69
- **Validation Warnings:** 78
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 41
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `20` | `20` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | defense | `2` | `2` |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `4` | `4` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 210 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 82 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `19` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `20` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 46 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 41 | START | 41 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `18` | `18` | 41 | START | 41 | 94 |
| ✅ EXACT | `Action_PassBlock` | LG | `19` | `19` | 41 | START | 41 | 129 |
| ✅ EXACT | `Action_PassBlock` | RT | `20` | `20` | 41 | START | 41 | 210 |
| ✅ EXACT | `Action_PassBlock` | RG | `21` | `21` | 41 | START | 41 | 167 |
| ✅ EXACT | `Action_RunOutRoute` | DE2 | `2` | `2` | 47 | START | 47 | 147 |
| ✅ EXACT | `Action_RunOutRoute` | WR2 | `4` | `4` | 47 | START | 47 | 110 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 47 | END | 47 | 47 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 86 | START | 86 | 96 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `4` | `4` | 111 | START | 111 | 119 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `4` | `4` | 120 | START | 120 | 197 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_SnapReceive` | 47 | 47 | 1 | inferred_complete_timeline |
| `Action_None` | 48 | 85 | 38 | inferred_complete_timeline |
| `Action_ThrowPass` | 86 | 96 | 11 | inferred_complete_timeline |
| `Action_None` | 97 | 210 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–137
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 90 | 112 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 121 | 128 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 137 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–197
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunOutRoute` | 47 | 110 | 64 | inferred_complete_timeline |
| `Action_SecureCatch` | 111 | 119 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 120 | 197 | 78 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_PreSnap` | 62 | 210 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–207
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 93 | 53 | inferred_complete_timeline |
| `Action_PassBlock` | 95 | 207 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 129 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 195

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 94 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 122 | 132 | 11 | inferred_complete_timeline |
| `Action_PassBlock` | 134 | 142 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 144 | 210 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 167 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_PassBlock` | 41 | 210 | 170 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 95 | 96 | inferred_complete_timeline |
| `Action_PreSnap` | 100 | 210 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_RunOutRoute` | 47 | 147 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 82 | 83 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 95 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 98 | 106 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 108 | 109 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 209 | 93 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 117 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

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
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 192 | 193 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 195 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 205 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 209 | 210 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 210 | 58 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
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
| `22` | `24` | Position_Unknown | Team_Unknown | 62–64 | 3 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 64–67 | 4 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 91–96 | 6 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 104–107 | 4 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 128–210 | 61 | 2 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 158–210 | 53 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 164–207 | 34 | 3 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 178–206 | 16 | 2 | Undefined position; Undefined team |
| `31` | `41` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF` position mapped to `defense` team
- ⚠️ 10 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 10 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 20 |
| Missing visible bounding boxes during action | 56 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-60] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunOutRoute' range [47-147] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [120-197] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-192] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-195] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-205] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [209-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-148] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [90-112] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [121-128] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-137] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-82] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-95] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [98-106] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-209] for track '11' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-117] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-95] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-93] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [95-207] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-94] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-116] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [122-132] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [134-142] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [144-210] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-129] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-210] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [41-167] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [62-64] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-96] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [104-107] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [128-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-210] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [164-172] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-177] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-207] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-210] for track '29' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [178-187] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-206] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-210] for track '31' has 1 frames without a visible bounding box.
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