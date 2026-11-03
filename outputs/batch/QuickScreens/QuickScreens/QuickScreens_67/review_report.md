# Play-Annotation-Generator Annotation Review — QuickScreens_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `QuickScreens_67`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_QuickScreens`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 95
- **Validation Warnings:** 101
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 6
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 81
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | offense | `4` | `4` |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | offense | `3` | `3` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | offense | `3` | `3` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `10` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 35 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `4` | `Group` | 0 | START | 0 | 31 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR5 | `8` | `Group` | 0 | START | 0 | 9 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 10 | START | 10 | 17 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 23 | END | 10 | 23 |
| ✅ EXACT | `Action_ScreenBlock` | WR2 | `4` | `4` | 32 | START | 32 | 119 |
| ✅ EXACT | `Action_ThrowScreenPass` | QB | `11` | `11` | 33 | START | 33 | 43 |
| ✅ EXACT | `Action_TurnToQuarterback` | WR1 | `3` | `3` | 36 | START | 36 | 49 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `3` | `3` | 58 | START | 58 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunAfterCatch` | WR1 | `3` | `3` | 83 | START | 83 | 136 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_SnapReceive` | 10 | 23 | 14 | inferred_complete_timeline |
| `Action_None` | 24 | 32 | 9 | inferred_complete_timeline |
| `Action_ThrowScreenPass` | 33 | 43 | 11 | inferred_complete_timeline |
| `Action_None` | 44 | 153 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 35 | 36 | inferred_complete_timeline |
| `Action_TurnToQuarterback` | 36 | 49 | 14 | inferred_complete_timeline |
| `Action_None` | 50 | 57 | 8 | inferred_complete_timeline |
| `Action_SecureCatch` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_None` | 67 | 82 | 16 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 83 | 136 | 54 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 138 | 139 | 2 | inferred_complete_timeline |
| `Action_RunAfterCatch` | 145 | 146 | 2 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 31 | 32 | inferred_complete_timeline |
| `Action_ScreenBlock` | 32 | 119 | 88 | inferred_complete_timeline |
| `Action_None` | 120 | 210 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–68
- **Visible Samples:** 66

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 61 | 52 | inferred_complete_timeline |
| `Action_None` | 64 | 65 | 2 | inferred_complete_timeline |
| `Action_None` | 67 | 68 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 173 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>WR5 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 79 | 70 | inferred_complete_timeline |
| `Action_None` | 83 | 127 | 45 | inferred_complete_timeline |
| `Action_None` | 135 | 146 | 12 | inferred_complete_timeline |
| `Action_None` | 149 | 150 | 2 | inferred_complete_timeline |
| `Action_None` | 152 | 210 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–44
- **Visible Samples:** 31

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_BallSnap` | 10 | 17 | 8 | inferred_complete_timeline |
| `Action_None` | 24 | 29 | 6 | inferred_complete_timeline |
| `Action_None` | 38 | 44 | 7 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 4 | 9 | 6 | inferred_complete_timeline |
| `Action_None` | 10 | 14 | 5 | inferred_complete_timeline |
| `Action_None` | 16 | 45 | 30 | inferred_complete_timeline |
| `Action_None` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 185 | 176 | inferred_complete_timeline |
| `Action_None` | 191 | 210 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 145 | 136 | inferred_complete_timeline |
| `Action_None` | 147 | 161 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 200 | 191 | inferred_complete_timeline |
| `Action_None` | 202 | 207 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–157
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 63 | 54 | inferred_complete_timeline |
| `Action_None` | 67 | 74 | 8 | inferred_complete_timeline |
| `Action_None` | 78 | 79 | 2 | inferred_complete_timeline |
| `Action_None` | 84 | 133 | 50 | inferred_complete_timeline |
| `Action_None` | 135 | 157 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–133
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 133 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 65 | 56 | inferred_complete_timeline |
| `Action_None` | 69 | 159 | 91 | inferred_complete_timeline |
| `Action_None` | 167 | 210 | 44 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_None` | 10 | 49 | 40 | inferred_complete_timeline |
| `Action_None` | 51 | 53 | 3 | inferred_complete_timeline |
| `Action_None` | 61 | 109 | 49 | inferred_complete_timeline |
| `Action_None` | 112 | 115 | 4 | inferred_complete_timeline |
| `Action_None` | 119 | 210 | 92 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `13` | Position_Unknown | Team_Unknown | 0–147 | 148 | 2 | Undefined position; Undefined team |
| `16` | `16` | Position_Unknown | Team_Unknown | 15–210 | 196 | 1 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 25–200 | 162 | 6 | Undefined position; Undefined team |
| `18` | `18` | Position_Unknown | Team_Unknown | 25–210 | 181 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 26–210 | 175 | 3 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 27–181 | 146 | 4 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 31–210 | 172 | 3 | Undefined position; Undefined team |
| `22` | `24` | Position_Unknown | Team_Unknown | 59–60 | 2 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 66–210 | 138 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 93–115 | 21 | 2 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 124–164 | 41 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 145–210 | 66 | 1 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 162–210 | 48 | 2 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 181–182 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunAfterCatch` and target `3` (3 segments found)

### Track Identity Issues

- ⚠️ 14 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 14 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 28 |
| Missing visible bounding boxes during action | 72 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_None' range [10-185] for track '0' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-65] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-159] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-210] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-49] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-53] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-109] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-210] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [83-136] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [138-139] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunAfterCatch' range [145-146] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ScreenBlock' range [32-119] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-173] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-145] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-161] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-133] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-79] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-127] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-146] for track '8' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-150] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-210] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-200] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-207] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-61] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-65] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-68] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-153] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-63] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-74] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-133] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-157] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-147] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [10-17] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-29] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [10-14] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [16-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-210] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [15-210] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-27] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [30-32] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-45] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-77] for track '17' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-192] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-200] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [25-48] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [54-210] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [26-29] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-137] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-210] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-49] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-75] for track '20' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-79] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-181] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-35] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-49] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-210] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-60] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-127] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-210] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-109] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-115] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-164] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-170] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-210] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-182] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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

</details>