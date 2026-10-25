# Play-Annotation-Generator Annotation Review — BootPass_15

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_15`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 92
- **Validation Warnings:** 82
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 8
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `16` | `16` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_SecureCatch` | WR2 | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 72 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `12` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 47 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `6` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 47 |
| ✅ EXACT | `Action_BallSnap` | C | `12` | `12` | 40 | START | 40 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `12` | `12` | 48 | START | 57 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `16` | `16` | 48 | START | 48 | 191 |
| ✅ EXACT | `Action_RunBlock` | LG | `18` | `18` | 48 | START | 48 | 72 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 48 | START | 48 | 54 |
| ✅ EXACT | `Action_RunBlock` | LT | `8` | `8` | 48 | START | 48 | 210 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 56 | END | 40 | 56 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `2` | `2` | 64 | START | 64 | 73 |
| ✅ EXACT | `Action_BootAway` | QB | `2` | `2` | 74 | START | 74 | 121 |
| ✅ EXACT | `Action_ThrowPass` | QB | `2` | `2` | 129 | START | 129 | 139 |
| ✅ EXACT | `Action_SecureCatch` | WR2 | `1` | `1` | 164 | START | 164 | 178 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_SnapReceive` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 57 | 63 | 7 | inferred_complete_timeline |
| `Action_FakeHandoff` | 64 | 73 | 10 | inferred_complete_timeline |
| `Action_BootAway` | 74 | 121 | 48 | inferred_complete_timeline |
| `Action_None` | 122 | 128 | 7 | inferred_complete_timeline |
| `Action_ThrowPass` | 129 | 139 | 11 | inferred_complete_timeline |
| `Action_None` | 140 | 187 | 48 | inferred_complete_timeline |
| `Action_None` | 189 | 204 | 16 | inferred_complete_timeline |
| `Action_None` | 206 | 210 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 128 | 89 | inferred_complete_timeline |
| `Action_None` | 133 | 138 | 6 | inferred_complete_timeline |
| `Action_None` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 148 | 2 | inferred_complete_timeline |
| `Action_None` | 151 | 154 | 4 | inferred_complete_timeline |
| `Action_None` | 164 | 165 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–188
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 74 | 81 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 84 | 123 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 128 | 163 | 36 | inferred_complete_timeline |
| `Action_SecureCatch` | 164 | 178 | 15 | inferred_complete_timeline |
| `Action_None` | 179 | 188 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 210 | 163 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–72
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 72 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–196
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_BallSnap` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 67 | 11 | inferred_complete_timeline |
| `Action_RunBlock` | 71 | 75 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 112 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 116 | 144 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 146 | 196 | 51 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 69

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 54 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 56 | 69 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–200
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 47 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 48 | 191 | 144 | inferred_complete_timeline |
| `Action_RunBlock` | 193 | 200 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 92 | 53 | inferred_complete_timeline |
| `Action_None` | 101 | 210 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–208
- **Visible Samples:** 187

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 128 | 89 | inferred_complete_timeline |
| `Action_None` | 131 | 140 | 10 | inferred_complete_timeline |
| `Action_None` | 143 | 144 | 2 | inferred_complete_timeline |
| `Action_None` | 147 | 150 | 4 | inferred_complete_timeline |
| `Action_None` | 155 | 164 | 10 | inferred_complete_timeline |
| `Action_None` | 166 | 170 | 5 | inferred_complete_timeline |
| `Action_None` | 174 | 175 | 2 | inferred_complete_timeline |
| `Action_None` | 179 | 193 | 15 | inferred_complete_timeline |
| `Action_None` | 197 | 204 | 8 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–101
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 101 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 119 | 80 | inferred_complete_timeline |
| `Action_None` | 132 | 210 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 210 | 171 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 206

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_None` | 40 | 189 | 150 | inferred_complete_timeline |
| `Action_None` | 195 | 210 | 16 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `21` | `22` | Position_Unknown | Team_Unknown | 13–24 | 6 | 2 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 50–204 | 152 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 92–101 | 10 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 102–128 | 27 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 154–208 | 55 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 164–184 | 6 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 175–190 | 12 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 180–186 | 6 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `17` (actor_track_id `17`): `SAF1` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [40–56], lower_priority='Action_RunBlock' annotated_start=48, effective_Action_RunBlock_start=57.
- ⚠️ Action 'Action_None' range [40-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [74-81] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [84-123] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-188] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-187] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-204] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-128] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-138] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-148] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-154] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-165] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-210] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-210] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-92] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-210] for track '10' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [40-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-67] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [71-75] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-112] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [116-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [146-196] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [193-200] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-189] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-72] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [48-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [56-69] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-128] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-140] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-144] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-164] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-170] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-175] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-193] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-204] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-16] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [23-24] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-124] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-204] for track '22' has 8 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-101] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-128] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-208] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-167] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-184] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-181] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-186] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-181] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-186] for track '28' has 2 frames without a visible bounding box.
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