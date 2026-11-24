# Play-Annotation-Generator Annotation Review — BootPass_120

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_120`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 40
- **Ball Tracks:** 1
- **Action Segments:** 97
- **Validation Warnings:** 122
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 2
- **Missing Segments:** 1
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 78
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `13` | `13` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `5` | `5` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `9` | `9` |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT1 | defense | `15` | `15` |
| ✅ EXACT | `Action_FakeHandoff` | DT1 | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | DT1 | defense | `15` | `15` |
| ⚠️ START CHANGED | `Action_ThrowPass` | DT1 | defense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF2 | defense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `13` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `14` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `3` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `5` | `Group` | 0 | START | 0 | 60 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `6` | `Group` | 0 | START | 0 | 50 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `9` | `Group` | 0 | START | 0 | 50 |
| ✅ EXACT | `Action_BallSnap` | C | `9` | `9` | 51 | START | 51 | 67 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `12` | `12` | 61 | START | 61 | 132 |
| ✅ EXACT | `Action_RunBlock` | LT | `13` | `13` | 61 | START | 61 | 64 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `3` | `3` | 61 | START | 61 | 84 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `5` | `5` | 61 | START | 61 | 98 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `9` | `9` | 61 | START | 69 | 73 |
| ⚠️ AMBIGUOUS MATCH | `Action_SnapReceive` | DT1 | `15` | `15` | 68 | END | 51 | 52 |
| ✅ EXACT | `Action_FakeHandoff` | DT1 | `15` | `15` | 70 | START | 70 | 92 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | DT1 | `15` | `15` | 93 | START | 93 | 128 |
| ⚠️ START CHANGED | `Action_ThrowPass` | DT1 | `15` | `15` | 135 | START | 136 | 145 |
| ❌ MISSING SEGMENT | `Action_SecureCatch` | SAF2 | `2` | `2` | 172 | START | N/A | N/A |

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
- **Visible Frames:** 0–269
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 51 | 1 | inferred_complete_timeline |
| `Action_None` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_None` | 80 | 110 | 31 | inferred_complete_timeline |
| `Action_None` | 112 | 122 | 11 | inferred_complete_timeline |
| `Action_None` | 124 | 132 | 9 | inferred_complete_timeline |
| `Action_None` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_None` | 145 | 146 | 2 | inferred_complete_timeline |
| `Action_None` | 175 | 177 | 3 | inferred_complete_timeline |
| `Action_None` | 255 | 269 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–142
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 84 | 34 | inferred_complete_timeline |
| `Action_None` | 87 | 94 | 8 | inferred_complete_timeline |
| `Action_None` | 96 | 102 | 7 | inferred_complete_timeline |
| `Action_None` | 107 | 113 | 7 | inferred_complete_timeline |
| `Action_None` | 118 | 136 | 19 | inferred_complete_timeline |
| `Action_None` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–114
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 72 | 22 | inferred_complete_timeline |
| `Action_None` | 79 | 114 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 88 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 64 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 84 | 24 | inferred_complete_timeline |
| `Action_RunBlock` | 90 | 92 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 98 | 100 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 105 | 126 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–73
- **Visible Samples:** 73

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_BallSnap` | 51 | 67 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 73 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–145
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 132 | 72 | inferred_complete_timeline |
| `Action_RunBlock` | 136 | 142 | 7 | inferred_complete_timeline |
| `Action_RunBlock` | 144 | 145 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–126
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 60 | 61 | inferred_complete_timeline |
| `Action_RunBlock` | 61 | 98 | 38 | inferred_complete_timeline |
| `Action_RunBlock` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 124 | 126 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 116 | 66 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 142 | 92 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–146
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_SnapReceive` | 51 | 52 | 2 | inferred_complete_timeline |
| `Action_SnapReceive` | 59 | 68 | 10 | inferred_complete_timeline |
| `Action_None` | 69 | 69 | 1 | inferred_complete_timeline |
| `Action_FakeHandoff` | 70 | 92 | 23 | inferred_complete_timeline |
| `Action_BootAway` | 93 | 128 | 36 | inferred_complete_timeline |
| `Action_BootAway` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_None` | 134 | 134 | 1 | inferred_complete_timeline |
| `Action_ThrowPass` | 136 | 145 | 10 | inferred_complete_timeline |
| `Action_None` | 146 | 146 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–151
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 146 | 96 | inferred_complete_timeline |
| `Action_None` | 150 | 151 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–163
- **Visible Samples:** 161

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 86 | 36 | inferred_complete_timeline |
| `Action_None` | 90 | 163 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–142
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 137 | 87 | inferred_complete_timeline |
| `Action_None` | 139 | 142 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 148

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 50 | 51 | inferred_complete_timeline |
| `Action_None` | 51 | 147 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–124
- **Visible Samples:** 124

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 115 | 116 | inferred_complete_timeline |
| `Action_PreSnap` | 117 | 124 | 8 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `17` | `18` | Position_Unknown | Team_Unknown | 75–77 | 3 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 77–161 | 85 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 89–142 | 53 | 2 | Undefined position; Undefined team |
| `20` | `21` | Position_Unknown | Team_Unknown | 92–269 | 175 | 3 | Undefined position; Undefined team |
| `21` | `22` | Position_Unknown | Team_Unknown | 97–100 | 4 | 1 | Undefined position; Undefined team |
| `22` | `23` | Position_Unknown | Team_Unknown | 101–146 | 41 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 131–144 | 12 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 143–269 | 127 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 143–166 | 24 | 1 | Undefined position; Undefined team |
| `26` | `28` | Position_Unknown | Team_Unknown | 144–269 | 126 | 1 | Undefined position; Undefined team |
| `27` | `29` | Position_Unknown | Team_Unknown | 147–150 | 4 | 1 | Undefined position; Undefined team |
| `28` | `30` | Position_Unknown | Team_Unknown | 147–242 | 83 | 2 | Undefined position; Undefined team |
| `29` | `31` | Position_Unknown | Team_Unknown | 148–269 | 122 | 1 | Undefined position; Undefined team |
| `30` | `32` | Position_Unknown | Team_Unknown | 148–160 | 13 | 1 | Undefined position; Undefined team |
| `31` | `33` | Position_Unknown | Team_Unknown | 148–149 | 2 | 1 | Undefined position; Undefined team |
| `32` | `35` | Position_Unknown | Team_Unknown | 156–269 | 114 | 1 | Undefined position; Undefined team |
| `33` | `36` | Position_Unknown | Team_Unknown | 156–157 | 2 | 1 | Undefined position; Undefined team |
| `35` | `38` | Position_Unknown | Team_Unknown | 167–168 | 2 | 1 | Undefined position; Undefined team |
| `36` | `39` | Position_Unknown | Team_Unknown | 169–268 | 100 | 1 | Undefined position; Undefined team |
| `37` | `40` | Position_Unknown | Team_Unknown | 225–269 | 44 | 2 | Undefined position; Undefined team |
| `38` | `41` | Position_Unknown | Team_Unknown | 235–269 | 35 | 1 | Undefined position; Undefined team |
| `39` | `43` | Position_Unknown | Team_Unknown | 260–263 | 4 | 1 | Undefined position; Undefined team |
| `40` | `45` | Position_Unknown | Team_Unknown | 265–269 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `34` | `37` | 156 | 156 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (3 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `5` (3 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `9` (C): Annotated start 61 != Inferred start 69
- ⚠️ Ambiguous match for action `Action_SnapReceive` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `15` (2 segments found)
- ⚠️ `Action_ThrowPass` for actor_track_id `15` (DT1): Annotated start 135 != Inferred start 136
- ❌ Missing segment for action `Action_SecureCatch` on target `2` (SAF2)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF2` position mapped to `defense` team
- ⚠️ 23 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 23 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 46 |
| Missing visible bounding boxes during action | 73 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Segment 'Action_SecureCatch' for track '2' has invalid range: start=172, end=124. Clamping end to start.
- ⚠️ Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [51–68], lower_priority='Action_RunBlock' annotated_start=61, effective_Action_RunBlock_start=69.
- ⚠️ Action 'Action_None' range [51-147] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-137] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-142] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-115] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-124] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [61-84] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [90-92] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [98-100] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [105-126] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [61-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [104-107] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [124-126] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-88] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-86] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-163] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-146] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [51-67] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-73] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-84] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-94] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-102] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-113] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-142] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-116] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [61-132] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [136-142] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [144-145] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [61-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [51-72] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-114] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [51-52] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [93-128] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 134, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [134-134] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 146, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [146-146] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-50] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '16' starts at frame 51, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [51-51] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-75] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-110] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-122] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-132] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-142] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-269] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [77-161] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-92] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-142] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-139] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-142] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-100] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-136] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-146] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-139] for track '23' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-166] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-150] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-163] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-242] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-269] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-160] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-149] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-157] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-268] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-267] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-263] for track '39' has 1 frames without a visible bounding box.
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

</details>