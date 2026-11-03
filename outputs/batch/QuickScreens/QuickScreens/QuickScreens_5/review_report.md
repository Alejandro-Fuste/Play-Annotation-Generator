# Play-Annotation-Generator Annotation Review — QuickScreens_5

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_5`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 44
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 160
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 6
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `19` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `1` | `1` |
| ✅ EXACT | `Action_SnapReceive` | TE1 | offense | `9` | `9` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowScreenPass` | TE1 | offense | `9` | `9` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 27 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `20` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 11 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `9` | `Group` | 0 | START | 0 | 11 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `19` | 12 | START | 12 | 24 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `1` | `1` | 28 | START | 28 | 86 |
| ✅ EXACT | `Action_SnapReceive` | TE1 | `9` | `9` | 28 | END | 12 | 28 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `0` | `0` | 28 | START | 28 | 61 |
| ✅ EXACT | `Action_ThrowScreenPass` | TE1 | `9` | `9` | 40 | START | 40 | 48 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 63 | START | 63 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | `0` | `0` | 76 | START | 76 | 140 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 67 | 56 | inferred_complete_timeline |
| `Action_None` | 74 | 210 | 137 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 28 | 61 | 34 | inferred_complete_timeline |
| `Action_None` | 62 | 62 | 1 | inferred_complete_timeline |
| `Action_SecureCatch` | 63 | 75 | 13 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 76 | 140 | 65 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 143 | 146 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–176
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 27 | 28 | inferred_complete_timeline |
| `Action_ScreenBlock` | 28 | 86 | 59 | inferred_complete_timeline |
| `Action_None` | 87 | 168 | 82 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_SnapReceive` | 12 | 28 | 17 | inferred_complete_timeline |
| `Action_None` | 29 | 39 | 11 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 40 | 48 | 9 | inferred_complete_timeline |
| `Action_None` | 49 | 201 | 153 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–32
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 32 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_BallSnap` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–41
- **Visible Samples:** 42

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 41 | 30 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–44
- **Visible Samples:** 29

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 30 | 2 | inferred_complete_timeline |
| `Action_None` | 43 | 44 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 59 | 48 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_None` | 91 | 92 | 2 | inferred_complete_timeline |
| `Action_None` | 131 | 137 | 7 | inferred_complete_timeline |
| `Action_None` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_None` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 162 | 166 | 5 | inferred_complete_timeline |
| `Action_None` | 169 | 170 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 210 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 24 | 13 | inferred_complete_timeline |
| `Action_None` | 29 | 32 | 4 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–65
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 51 | 40 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–192
- **Visible Samples:** 172

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 147 | 136 | inferred_complete_timeline |
| `Action_None` | 154 | 163 | 10 | inferred_complete_timeline |
| `Action_None` | 171 | 182 | 12 | inferred_complete_timeline |
| `Action_None` | 191 | 192 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–75
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 75 | 64 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 52 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 197 | 186 | inferred_complete_timeline |
| `Action_None` | 200 | 210 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 138 | 127 | inferred_complete_timeline |
| `Action_None` | 148 | 149 | 2 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 194 | 196 | 3 | inferred_complete_timeline |
| `Action_None` | 198 | 199 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–53
- **Visible Samples:** 54

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 11 | 12 | inferred_complete_timeline |
| `Action_None` | 12 | 53 | 42 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `6` | `6` | Position_Unknown | Team_Unknown | 0–39 | 40 | 2 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 58–185 | 115 | 6 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 70–210 | 135 | 4 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 71–76 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 98–210 | 101 | 4 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 101–123 | 23 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 110–210 | 101 | 1 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 114–210 | 64 | 10 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 115–201 | 50 | 6 | Undefined position; Undefined team |
| `30` | `37` | Position_Unknown | Team_Unknown | 115–210 | 88 | 3 | Undefined position; Undefined team |
| `31` | `39` | Position_Unknown | Team_Unknown | 118–210 | 78 | 5 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 119–210 | 64 | 5 | Undefined position; Undefined team |
| `33` | `44` | Position_Unknown | Team_Unknown | 123–210 | 86 | 2 | Undefined position; Undefined team |
| `34` | `49` | Position_Unknown | Team_Unknown | 132–210 | 69 | 4 | Undefined position; Undefined team |
| `35` | `50` | Position_Unknown | Team_Unknown | 137–140 | 4 | 1 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 138–140 | 3 | 1 | Undefined position; Undefined team |
| `37` | `53` | Position_Unknown | Team_Unknown | 155–210 | 56 | 1 | Undefined position; Undefined team |
| `38` | `61` | Position_Unknown | Team_Unknown | 165–210 | 32 | 4 | Undefined position; Undefined team |
| `39` | `62` | Position_Unknown | Team_Unknown | 170–171 | 2 | 1 | Undefined position; Undefined team |
| `40` | `64` | Position_Unknown | Team_Unknown | 190–210 | 21 | 1 | Undefined position; Undefined team |
| `41` | `66` | Position_Unknown | Team_Unknown | 194–210 | 17 | 1 | Undefined position; Undefined team |
| `42` | `67` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |
| `43` | `68` | Position_Unknown | Team_Unknown | 209–210 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 112 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 9: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_RunAfterCatch' range [76-140] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [143-146] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-168] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-32] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-59] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-87] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-147] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-160] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-166] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-170] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-41] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-39] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-197] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-210] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-67] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-201] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-75] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-147] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-163] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-182] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-192] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-138] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-196] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-53] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-52] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-51] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-30] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [43-44] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [12-24] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-32] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [12-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-61] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-142] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-178] for track '22' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-185] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-76] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-159] for track '23' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-180] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-76] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-142] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-210] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-116] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-123] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-130] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-144] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-177] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-182] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-128] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-141] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-171] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-201] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-119] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-143] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-144] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-152] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-159] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-175] for track '31' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-127] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-164] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-177] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-210] for track '32' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-153] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-210] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-178] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-200] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-206] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-140] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-210] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-173] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-210] for track '38' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-171] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-210] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-210] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-210] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '6' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '6' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.

</details>