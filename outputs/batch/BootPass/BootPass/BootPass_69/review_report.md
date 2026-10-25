# Play-Annotation-Generator Annotation Review — BootPass_69

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_69`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 98
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 8
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 76
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `21` | `21` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `12` | `12` |
| ✅ EXACT | `Action_SecureCatch` | WR3 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 179 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `12` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `16` | `Group` | 0 | START | 0 | 36 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `18` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 44 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 36 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 37 | START | 37 | 51 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `14` | `14` | 45 | START | 52 | 197 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `18` | `18` | 45 | START | 45 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `19` | `19` | 45 | START | 45 | 48 |
| ✅ EXACT | `Action_RunBlock` | LG | `20` | `20` | 45 | START | 45 | 210 |
| ✅ EXACT | `Action_RunBlock` | RG | `21` | `21` | 45 | START | 45 | 72 |
| ✅ EXACT | `Action_SnapReceive` | QB | `12` | `12` | 51 | END | 37 | 51 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `12` | `12` | 57 | START | 57 | 72 |
| ✅ EXACT | `Action_BootAway` | QB | `12` | `12` | 73 | START | 73 | 126 |
| ✅ EXACT | `Action_ThrowPass` | QB | `12` | `12` | 146 | START | 146 | 155 |
| ✅ EXACT | `Action_SecureCatch` | WR3 | `0` | `0` | 180 | START | 180 | 186 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_SnapReceive` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_None` | 52 | 56 | 5 | inferred_complete_timeline |
| `Action_FakeHandoff` | 57 | 72 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 73 | 126 | 54 | inferred_complete_timeline |
| `Action_None` | 127 | 145 | 19 | inferred_complete_timeline |
| `Action_ThrowPass` | 146 | 155 | 10 | inferred_complete_timeline |
| `Action_None` | 156 | 198 | 43 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 114 | 78 | inferred_complete_timeline |
| `Action_None` | 116 | 122 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 179 | 180 | inferred_complete_timeline |
| `Action_SecureCatch` | 180 | 186 | 7 | inferred_complete_timeline |
| `Action_None` | 187 | 206 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–156
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 95 | 59 | inferred_complete_timeline |
| `Action_None` | 102 | 156 | 55 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–140
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 67 | 23 | inferred_complete_timeline |
| `Action_RunBlock` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 210 | 166 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_BallSnap` | 37 | 51 | 15 | inferred_complete_timeline |
| `Action_RunBlock` | 52 | 197 | 146 | inferred_complete_timeline |
| `Action_RunBlock` | 208 | 210 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 72 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 156

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 44 | 45 | inferred_complete_timeline |
| `Action_RunBlock` | 45 | 48 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 81 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 104 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 107 | 194 | 88 | inferred_complete_timeline |
| `Action_RunBlock` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 160 | 124 | inferred_complete_timeline |
| `Action_None` | 162 | 210 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–190
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 87 | 51 | inferred_complete_timeline |
| `Action_None` | 96 | 176 | 81 | inferred_complete_timeline |
| `Action_None` | 189 | 190 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 125

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 124 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 208

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 59 | 23 | inferred_complete_timeline |
| `Action_None` | 61 | 62 | 2 | inferred_complete_timeline |
| `Action_None` | 64 | 197 | 134 | inferred_complete_timeline |
| `Action_None` | 199 | 210 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 122 | 86 | inferred_complete_timeline |
| `Action_None` | 128 | 210 | 83 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–137
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 129 | 93 | inferred_complete_timeline |
| `Action_None` | 134 | 137 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 197 | 161 | inferred_complete_timeline |
| `Action_None` | 199 | 200 | 2 | inferred_complete_timeline |
| `Action_None` | 204 | 210 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 36 | 37 | inferred_complete_timeline |
| `Action_None` | 37 | 210 | 174 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 53–210 | 132 | 4 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 91–107 | 12 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 91–93 | 3 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 109–210 | 100 | 3 | Undefined position; Undefined team |
| `26` | `27` | Position_Unknown | Team_Unknown | 118–128 | 10 | 2 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 144–147 | 4 | 1 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 150–151 | 2 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 153–163 | 8 | 2 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 166–210 | 45 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 170–172 | 3 | 1 | Undefined position; Undefined team |
| `33` | `40` | Position_Unknown | Team_Unknown | 173–181 | 8 | 2 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 180–181 | 2 | 1 | Undefined position; Undefined team |
| `35` | `44` | Position_Unknown | Team_Unknown | 181–210 | 25 | 3 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 188–190 | 3 | 1 | Undefined position; Undefined team |
| `37` | `47` | Position_Unknown | Team_Unknown | 203–210 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `14` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (5 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF3` position mapped to `defense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF2` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [37–51], lower_priority='Action_RunBlock' annotated_start=45, effective_Action_RunBlock_start=52.
- ⚠️ Action 'Action_None' range [187-206] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-122] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-160] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-122] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-59] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-62] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-197] for track '5' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-197] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-87] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-176] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-95] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-156] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-198] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-129] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-137] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [52-197] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [208-210] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-124] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-67] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [139-140] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-48] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [80-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [103-104] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [107-194] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [196-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-210] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [45-72] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [73-198] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-99] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-107] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-93] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-122] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-175] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-210] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-163] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-172] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-178] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-191] for track '35' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-210] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '37' has 2 frames without a visible bounding box.
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

</details>