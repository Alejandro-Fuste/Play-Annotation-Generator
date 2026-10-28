# Play-Annotation-Generator Annotation Review — Draw_51

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Draw_51`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Draw`
- **Result:** `Result_Touchdown`
- **Result Frame:** 299
- **Player Tracks:** 36
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 84
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
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `22` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `14` | `13` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `16` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `22` | `21` |
| ✅ EXACT | `Action_PassBlock` | RT | offense | `6` | `5` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | offense | `19` | `18` |
| ✅ EXACT | `Action_BallCarry` | WR2 | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 5 | START | 5 | 106 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `12` | `Group` | 5 | START | 5 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `14` | `Group` | 5 | START | 5 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 5 | START | 5 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 5 | START | 5 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 5 | START | 5 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `22` | `Group` | 5 | START | 5 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 5 | START | 5 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 5 | START | 5 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `6` | `Group` | 5 | START | 5 | 48 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `9` | `Group` | 5 | START | 5 | 45 |
| ✅ EXACT | `Action_BallSnap` | C | `21` | `20` | 46 | START | 46 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `14` | `13` | 49 | START | 49 | 139 |
| ✅ EXACT | `Action_PassBlock` | LG | `16` | `15` | 49 | START | 49 | 96 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `20` | 49 | START | 63 | 152 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `22` | `21` | 49 | START | 49 | 85 |
| ✅ EXACT | `Action_PassBlock` | RT | `6` | `5` | 49 | START | 49 | 146 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `18` | 62 | END | 46 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakePassDroptoHandoff` | QB | `19` | `18` | 66 | START | 66 | 152 |
| ✅ EXACT | `Action_BallCarry` | WR2 | `1` | `0` | 107 | START | 107 | 299 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 163 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 5–190
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_SnapReceive` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_None` | 63 | 65 | 3 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 66 | 152 | 87 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 154 | 168 | 15 | inferred_complete_timeline |
| `Action_FakePassDroptoHandoff` | 171 | 190 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 100 | 55 | inferred_complete_timeline |
| `Action_None` | 109 | 195 | 87 | inferred_complete_timeline |
| `Action_None` | 201 | 205 | 5 | inferred_complete_timeline |
| `Action_None` | 211 | 217 | 7 | inferred_complete_timeline |
| `Action_None` | 219 | 246 | 28 | inferred_complete_timeline |
| `Action_None` | 249 | 299 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 159 | 114 | inferred_complete_timeline |
| `Action_None` | 162 | 263 | 102 | inferred_complete_timeline |
| `Action_None` | 265 | 299 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 106 | 102 | inferred_complete_timeline |
| `Action_BallCarry` | 107 | 299 | 193 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 5–120
- **Visible Samples:** 116

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 120 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 5–168
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 168 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 139 | 91 | inferred_complete_timeline |
| `Action_PassBlock` | 146 | 163 | 18 | inferred_complete_timeline |
| `Action_None` | 164 | 299 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 5–96
- **Visible Samples:** 92

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 96 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 285

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_BallSnap` | 46 | 62 | 17 | inferred_complete_timeline |
| `Action_PassBlock` | 63 | 152 | 90 | inferred_complete_timeline |
| `Action_PassBlock` | 160 | 163 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 189 | 26 | inferred_complete_timeline |
| `Action_None` | 192 | 197 | 6 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `offense`
- **Visible Frames:** 5–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 85 | 37 | inferred_complete_timeline |
| `Action_PassBlock` | 88 | 163 | 76 | inferred_complete_timeline |
| `Action_None` | 164 | 299 | 136 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–146
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 48 | 44 | inferred_complete_timeline |
| `Action_PassBlock` | 49 | 146 | 98 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 5–160
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 147 | 102 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 151 | 106 | inferred_complete_timeline |
| `Action_None` | 154 | 248 | 95 | inferred_complete_timeline |
| `Action_None` | 250 | 299 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 182 | 137 | inferred_complete_timeline |
| `Action_None` | 185 | 189 | 5 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 172 | 127 | inferred_complete_timeline |
| `Action_None` | 174 | 299 | 126 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 110 | 65 | inferred_complete_timeline |
| `Action_None` | 113 | 190 | 78 | inferred_complete_timeline |
| `Action_None` | 192 | 198 | 7 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 136 | 91 | inferred_complete_timeline |
| `Action_None` | 140 | 149 | 10 | inferred_complete_timeline |
| `Action_None` | 151 | 299 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 299 | 254 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 5–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 45 | 41 | inferred_complete_timeline |
| `Action_None` | 46 | 225 | 180 | inferred_complete_timeline |
| `Action_None` | 228 | 299 | 72 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 103–115 | 10 | 2 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 120–122 | 3 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 121–127 | 7 | 1 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 127–299 | 173 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 144–158 | 6 | 2 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 152–299 | 148 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 167–299 | 132 | 2 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 175–191 | 17 | 1 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 187–299 | 111 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 194–299 | 105 | 2 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 264–299 | 36 | 1 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 269–271 | 3 | 1 | Undefined position; Undefined team |
| `34` | `45` | Position_Unknown | Team_Unknown | 287–288 | 2 | 1 | Undefined position; Undefined team |
| `35` | `47` | Position_Unknown | Team_Unknown | 293–294 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `22` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakePassDroptoHandoff` and target `19` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `18`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `20`): `SAF1` position mapped to `defense` team
- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 54 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [46–62], lower_priority='Action_PassBlock' annotated_start=49, effective_Action_PassBlock_start=63.
- ⚠️ Action 'Action_None' range [46-299] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-110] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-198] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-168] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-146] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-136] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-149] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-159] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-263] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-182] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-189] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-172] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-100] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-195] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-205] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-217] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-246] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-139] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-160] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-96] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-151] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-248] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [250-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-225] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [66-152] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [154-168] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakePassDroptoHandoff' range [171-190] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-299] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [63-152] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-189] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [49-85] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-299] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-110] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-115] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-122] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-127] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-158] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-299] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-191] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-199] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [264-299] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-271] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [287-288] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '35' has 1 frames without a visible bounding box.
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

</details>