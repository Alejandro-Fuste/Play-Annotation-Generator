# Play-Annotation-Generator Annotation Review — OutRoutes_111

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OutRoutes_111`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_OutRoutes`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 108
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `5` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `12` | `12` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `3` | `3` |
| ✅ EXACT | `Action_BallCarry` | WR3 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 0 | START | 0 | 58 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `11` | `Group` | 0 | START | 0 | 79 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `3` | `Group` | 0 | START | 0 | 32 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 92 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `5` | `Group` | 0 | START | 0 | 210 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `12` | `12` | 28 | START | 28 | 65 |
| ✅ EXACT | `Action_PassBlock` | LT | `15` | `15` | 28 | START | 28 | 145 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 28 | START | 28 | 141 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `19` | `19` | 28 | START | 28 | 47 |
| ✅ EXACT | `Action_PassBlock` | RG | `20` | `20` | 28 | START | 28 | 160 |
| ✅ EXACT | `Action_RunOutRoute` | WR3 | `3` | `3` | 33 | START | 33 | 97 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 33 | END | 33 | 33 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 69 | START | 69 | 79 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `3` | `3` | 98 | START | 98 | 118 |
| ✅ EXACT | `Action_BallCarry` | WR3 | `3` | `3` | 119 | START | 119 | 187 |

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
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_SnapReceive` | 33 | 33 | 1 | inferred_complete_timeline |
| `Action_None` | 34 | 68 | 35 | inferred_complete_timeline |
| `Action_ThrowPass` | 69 | 79 | 11 | inferred_complete_timeline |
| `Action_None` | 80 | 144 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–79
- **Visible Samples:** 80

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 79 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–101
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 94 | 101 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 82 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–187
- **Visible Samples:** 188

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 32 | 33 | inferred_complete_timeline |
| `Action_RunOutRoute` | 33 | 97 | 65 | inferred_complete_timeline |
| `Action_SecureCatch` | 98 | 118 | 21 | inferred_complete_timeline |
| `Action_BallCarry` | 119 | 187 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `5`</summary>

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
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 145 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–141
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 141 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–143
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 47 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 56 | 57 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 59 | 143 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–160
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 160 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–148
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_PassBlock` | 28 | 65 | 38 | inferred_complete_timeline |
| `Action_PassBlock` | 67 | 148 | 82 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–122
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 38 | 39 | inferred_complete_timeline |
| `Action_PreSnap` | 40 | 122 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–155
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 155 | 156 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–143
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 159 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–156
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 151 | 152 | inferred_complete_timeline |
| `Action_PreSnap` | 155 | 156 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–107
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 107 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–209
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 209 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 210 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 120 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 58 | 59 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 36–210 | 168 | 4 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 61–81 | 13 | 3 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 64–148 | 72 | 2 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 65–71 | 7 | 1 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 66–68 | 3 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 77–123 | 35 | 4 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 88–152 | 37 | 4 | Undefined position; Undefined team |
| `29` | `32` | Position_Unknown | Team_Unknown | 91–151 | 61 | 1 | Undefined position; Undefined team |
| `30` | `33` | Position_Unknown | Team_Unknown | 93–158 | 49 | 5 | Undefined position; Undefined team |
| `31` | `34` | Position_Unknown | Team_Unknown | 108–148 | 21 | 6 | Undefined position; Undefined team |
| `32` | `37` | Position_Unknown | Team_Unknown | 116–179 | 22 | 3 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 119–132 | 9 | 2 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 124–148 | 13 | 3 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 156–159 | 4 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 163–164 | 2 | 1 | Undefined position; Undefined team |
| `37` | `43` | Position_Unknown | Team_Unknown | 200–210 | 11 | 1 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 204–210 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `21` (actor_track_id `21`): `SAF` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 72 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-82] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-151] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-156] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-38] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [40-122] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [119-187] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [94-101] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-155] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [67-148] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-107] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-159] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-145] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-144] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-210] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-141] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [56-57] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [59-143] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [28-160] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-58] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-39] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [42-43] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [48-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-210] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-67] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-81] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [64-67] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [81-148] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-71] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [66-68] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [77-78] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-91] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [95-101] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [103-123] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [88-89] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [92-100] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [111-133] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [150-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-151] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-97] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-112] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-122] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-145] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [155-158] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [108-109] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [114-115] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [118-119] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-135] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-140] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-148] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-120] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [160-162] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-179] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-123] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [129-132] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-125] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [137-139] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [141-148] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-159] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-164] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-210] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-210] for track '38' has 1 frames without a visible bounding box.
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

</details>