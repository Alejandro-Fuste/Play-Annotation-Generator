# Play-Annotation-Generator Annotation Review — BootPass_104

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_104`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 269
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 102
- **Validation Warnings:** 92
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 83
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `1` | `1` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `8` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | SAF1 | defense | `6` | `6` |
| ✅ EXACT | `Action_FakeHandoff` | SAF1 | defense | `6` | `6` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_BootAway` | SAF1 | defense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | defense | `6` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | TE | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB2 | `3` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB1 | `4` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 0 | START | 0 | 37 |
| ✅ EXACT | `Action_RunBlock` | LT | `1` | `1` | 38 | START | 38 | 150 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `14` | `14` | 38 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `18` | `18` | 38 | START | 38 | 69 |
| ✅ EXACT | `Action_RunBlock` | LG | `8` | `8` | 38 | START | 38 | 158 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `9` | `9` | 38 | START | 38 | 136 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | SAF1 | `6` | `6` | 44 | END | N/A | N/A |
| ✅ EXACT | `Action_FakeHandoff` | SAF1 | `6` | `6` | 47 | START | 47 | 70 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 51 | START | 51 | 51 |
| ✅ EXACT | `Action_BootAway` | SAF1 | `6` | `6` | 72 | START | 72 | 101 |
| ✅ EXACT | `Action_ThrowPass` | SAF1 | `6` | `6` | 103 | START | 103 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_SecureCatch` | TE | `0` | `0` | 143 | START | 143 | 152 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 269 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>RB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 269 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>RB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 259

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 86 | 36 | inferred_complete_timeline |
| `Action_None` | 89 | 148 | 60 | inferred_complete_timeline |
| `Action_None` | 150 | 191 | 42 | inferred_complete_timeline |
| `Action_None` | 193 | 246 | 54 | inferred_complete_timeline |
| `Action_None` | 254 | 269 | 16 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 230

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 124 | 125 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 142 | 1 | inferred_complete_timeline |
| `Action_SecureCatch` | 143 | 152 | 10 | inferred_complete_timeline |
| `Action_SecureCatch` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_None` | 156 | 181 | 26 | inferred_complete_timeline |
| `Action_None` | 186 | 241 | 56 | inferred_complete_timeline |
| `Action_None` | 260 | 269 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–150
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 150 | 113 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–158
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 158 | 121 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_None` | 38 | 50 | 13 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 52 | 146 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 265

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 136 | 99 | inferred_complete_timeline |
| `Action_RunBlock` | 139 | 203 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 207 | 269 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–260
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 38 | 69 | 32 | inferred_complete_timeline |
| `Action_RunBlock` | 83 | 137 | 55 | inferred_complete_timeline |
| `Action_RunBlock` | 144 | 148 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 150 | 260 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–149
- **Visible Samples:** 150

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 149 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–85
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 85 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–67
- **Visible Samples:** 68

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 67 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 69 | 19 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 121 | 71 | inferred_complete_timeline |
| `Action_None` | 123 | 125 | 3 | inferred_complete_timeline |
| `Action_None` | 130 | 134 | 5 | inferred_complete_timeline |
| `Action_None` | 138 | 140 | 3 | inferred_complete_timeline |
| `Action_None` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_None` | 145 | 149 | 5 | inferred_complete_timeline |
| `Action_None` | 153 | 220 | 68 | inferred_complete_timeline |
| `Action_None` | 222 | 239 | 18 | inferred_complete_timeline |
| `Action_None` | 243 | 269 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 269 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–242
- **Visible Samples:** 233

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 112 | 62 | inferred_complete_timeline |
| `Action_None` | 114 | 133 | 20 | inferred_complete_timeline |
| `Action_None` | 135 | 186 | 52 | inferred_complete_timeline |
| `Action_None` | 188 | 191 | 4 | inferred_complete_timeline |
| `Action_None` | 193 | 226 | 34 | inferred_complete_timeline |
| `Action_None` | 228 | 229 | 2 | inferred_complete_timeline |
| `Action_None` | 235 | 242 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 117 | 67 | inferred_complete_timeline |
| `Action_None` | 139 | 140 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 46 | 47 | inferred_complete_timeline |
| `Action_FakeHandoff` | 47 | 70 | 24 | inferred_complete_timeline |
| `Action_None` | 71 | 71 | 1 | inferred_complete_timeline |
| `Action_BootAway` | 72 | 101 | 30 | inferred_complete_timeline |
| `Action_None` | 102 | 102 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 103 | 113 | 11 | inferred_complete_timeline |
| `Action_None` | 114 | 150 | 37 | inferred_complete_timeline |
| `Action_None` | 153 | 269 | 117 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 268

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 250 | 200 | inferred_complete_timeline |
| `Action_None` | 253 | 269 | 17 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `12` | `12` | Position_Unknown | Team_Unknown | 0–269 | 250 | 3 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–143 | 80 | 5 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 2–155 | 91 | 3 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 85–94 | 7 | 2 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 126–156 | 31 | 1 | Undefined position; Undefined team |
| `24` | `31` | Position_Unknown | Team_Unknown | 146–161 | 16 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 153–269 | 117 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 154–269 | 111 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 159–269 | 111 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 160–161 | 2 | 1 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 161–269 | 108 | 2 | Undefined position; Undefined team |
| `30` | `42` | Position_Unknown | Team_Unknown | 182–263 | 81 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunBlock` on target `14` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `6` (SAF1)
- ⚠️ Ambiguous match for action `Action_SecureCatch` and target `0` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 64 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_SnapReceive' for track '6' has invalid range: start=51, end=44. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '14' has invalid range: start=51, end=44. Clamping end to start.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [51–51], lower_priority='Action_RunBlock' annotated_start=38, effective_Action_RunBlock_start=52.
- ⚠️ Action 'Action_PreSnap' range [0-124] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SecureCatch' range [143-152] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-181] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-241] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-269] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-150] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-250] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-86] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-148] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-191] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-246] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-269] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-121] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-125] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-134] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-140] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-150] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-269] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-140] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-158] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-136] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [139-203] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-85] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-244] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-269] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [52-146] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-112] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-133] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-186] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-191] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-226] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-229] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [38-69] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [83-137] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [144-148] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [150-260] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-57] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-133] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-69] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [2-3] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [6-7] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-155] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [85-89] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-156] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-161] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-179] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-186] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-204] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-186] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-263] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Player track '12' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '12' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>