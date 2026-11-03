# Play-Annotation-Generator Annotation Review — StopAndGo_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `StopAndGo_9`
- **Frame Range:** 0 to 359 (360 total frames)
- **Play:** `Play_Pass_StopAndGo`
- **Result:** `Result_Touchdown`
- **Result Frame:** 359
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 87
- **Validation Warnings:** 86
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 66
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `21` | `21` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | TE1 | offense | `11` | `11` |
| ✅ EXACT | `Action_VerticalStem` | TE1 | offense | `11` | `11` |
| ✅ EXACT | `Action_SellStop` | TE1 | offense | `11` | `11` |
| ✅ EXACT | `Action_RunGoRoute` | TE1 | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `11` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `12` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `15` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 104 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `18` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `21` | `Group` | 0 | START | 0 | 14 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `4` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 12 | START | 12 | 28 |
| ✅ EXACT | `Action_PassBlock` | RT | `12` | `12` | 15 | START | 15 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `16` | `16` | 15 | START | 29 | 37 |
| ✅ EXACT | `Action_PassBlock` | RG | `19` | `19` | 15 | START | 15 | 166 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `20` | `20` | 15 | START | 15 | 137 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `21` | `21` | 15 | START | 15 | 50 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | TE1 | `11` | `11` | 28 | END | N/A | N/A |
| ✅ EXACT | `Action_VerticalStem` | TE1 | `11` | `11` | 28 | START | 28 | 77 |
| ✅ EXACT | `Action_SellStop` | TE1 | `11` | `11` | 78 | START | 78 | 94 |
| ✅ EXACT | `Action_RunGoRoute` | TE1 | `11` | `11` | 95 | START | 95 | 205 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 105 | START | 105 | 115 |

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
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 104 | 105 | inferred_complete_timeline |
| `Action_ThrowPass` | 105 | 115 | 11 | inferred_complete_timeline |
| `Action_None` | 116 | 140 | 25 | inferred_complete_timeline |
| `Action_None` | 143 | 160 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–162
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 103 | 92 | inferred_complete_timeline |
| `Action_None` | 156 | 162 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–193
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 105 | 94 | inferred_complete_timeline |
| `Action_None` | 107 | 108 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 132 | 2 | inferred_complete_timeline |
| `Action_None` | 135 | 193 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 359 | 348 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_VerticalStem` | 28 | 77 | 50 | inferred_complete_timeline |
| `Action_SellStop` | 78 | 94 | 17 | inferred_complete_timeline |
| `Action_RunGoRoute` | 95 | 205 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–177
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_None` | 80 | 90 | 11 | inferred_complete_timeline |
| `Action_None` | 139 | 177 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–119
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 50 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 57 | 119 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 158

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 137 | 123 | inferred_complete_timeline |
| `Action_PassBlock` | 143 | 147 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 159 | 6 | inferred_complete_timeline |
| `Action_PassBlock` | 161 | 169 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 29 | 37 | 9 | inferred_complete_timeline |
| `Action_PassBlock` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 102 | 130 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 137 | 153 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–166
- **Visible Samples:** 167

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 166 | 152 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–84
- **Visible Samples:** 85

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 14 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 15 | 84 | 70 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 85 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–176
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 176 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–90
- **Visible Samples:** 91

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 90 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 183 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 122 | 111 | inferred_complete_timeline |
| `Action_None` | 137 | 170 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–113
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 113 | 102 | inferred_complete_timeline |

</details>

<details>
<summary>OLB — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 131 | 120 | inferred_complete_timeline |
| `Action_None` | 137 | 160 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 119 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–352
- **Visible Samples:** 341

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 100 | 89 | inferred_complete_timeline |
| `Action_None` | 107 | 344 | 238 | inferred_complete_timeline |
| `Action_None` | 351 | 352 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–359
- **Visible Samples:** 360

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 359 | 348 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–206
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 152 | 141 | inferred_complete_timeline |
| `Action_None` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 162 | 163 | 2 | inferred_complete_timeline |
| `Action_None` | 170 | 171 | 2 | inferred_complete_timeline |
| `Action_None` | 176 | 181 | 6 | inferred_complete_timeline |
| `Action_None` | 185 | 206 | 22 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 23–27 | 5 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 91–179 | 68 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 132–162 | 31 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 146–160 | 13 | 2 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 148–151 | 4 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 170–173 | 4 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 178–179 | 2 | 1 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 182–187 | 6 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 207–268 | 18 | 4 | Undefined position; Undefined team |
| `32` | `42` | Position_Unknown | Team_Unknown | 268–275 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `11` (TE1)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 60 |
| Track-related warning | 2 |
| Other | 2 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
- ⚠️ Overlapping action conflict at frame 28 for track '11': 'Action_SnapReceive' vs 'Action_VerticalStem'. Overriding with 'Action_VerticalStem'.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [12–28], lower_priority='Action_PassBlock' annotated_start=15, effective_Action_PassBlock_start=29.
- ⚠️ Action 'Action_None' range [12-131] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-160] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-359] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-100] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-344] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-352] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-183] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-105] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-132] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-193] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-113] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-90] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-122] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-170] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-119] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-152] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-181] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-206] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunGoRoute' range [95-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-84] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-176] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-85] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-103] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-162] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [29-37] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [45-48] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [102-130] for track '16' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [137-153] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-140] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-160] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-59] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-90] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-177] for track '18' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-166] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-137] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [143-147] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [161-169] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [15-50] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [57-119] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [23-27] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-129] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-179] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-162] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-160] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-151] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-173] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-179] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-187] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-211] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-241] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-250] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-268] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-275] for track '32' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_StopAndGo'.

</details>