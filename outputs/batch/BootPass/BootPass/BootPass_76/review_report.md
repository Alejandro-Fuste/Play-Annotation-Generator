# Play-Annotation-Generator Annotation Review — BootPass_76

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_76`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 1
- **Action Segments:** 68
- **Validation Warnings:** 60
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
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 46
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `4` | `4` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `12` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_RunBlock` | C | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `6` | `6` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `11` | `11` |
| ✅ EXACT | `Action_SecureCatch` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 152 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `11` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `13` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `17` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `4` | `Group` | 0 | START | 0 | 28 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `6` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `8` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `9` | `Group` | 0 | START | 0 | 28 |
| ✅ EXACT | `Action_BallSnap` | C | `4` | `4` | 29 | START | 29 | 45 |
| ✅ EXACT | `Action_RunBlock` | RG | `12` | `12` | 35 | START | 35 | 144 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RT | `16` | `16` | 35 | START | 35 | 96 |
| ⚠️ START CHANGED | `Action_RunBlock` | C | `4` | `4` | 35 | START | 46 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `6` | `6` | 35 | START | 35 | 47 |
| ✅ EXACT | `Action_RunBlock` | LT | `8` | `8` | 35 | START | 35 | 55 |
| ✅ EXACT | `Action_SnapReceive` | QB | `11` | `11` | 45 | END | 29 | 45 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `11` | `11` | 48 | START | 48 | 66 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | `11` | `11` | 67 | START | 67 | 89 |
| ✅ EXACT | `Action_ThrowPass` | QB | `11` | `11` | 121 | START | 121 | 131 |
| ✅ EXACT | `Action_SecureCatch` | WR1 | `0` | `0` | 153 | START | 153 | 160 |

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
- **Visible Frames:** 0–210
- **Visible Samples:** 205

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_None` | 46 | 47 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 48 | 66 | 19 | inferred_complete_timeline |
| `Action_BootAway` | 67 | 89 | 23 | inferred_complete_timeline |
| `Action_BootAway` | 94 | 116 | 23 | inferred_complete_timeline |
| `Action_None` | 117 | 120 | 4 | inferred_complete_timeline |
| `Action_ThrowPass` | 121 | 131 | 11 | inferred_complete_timeline |
| `Action_None` | 132 | 200 | 69 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–63
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 63 | 35 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 152 | 153 | inferred_complete_timeline |
| `Action_SecureCatch` | 153 | 160 | 8 | inferred_complete_timeline |
| `Action_None` | 161 | 210 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 209

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 43 | 15 | inferred_complete_timeline |
| `Action_None` | 46 | 210 | 165 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 66 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–54
- **Visible Samples:** 55

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 54 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–55
- **Visible Samples:** 56

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 55 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–111
- **Visible Samples:** 110

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 47 | 13 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 111 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–122
- **Visible Samples:** 123

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 29 | 45 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 122 | 77 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 145

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 144 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 96 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 149 | 49 | inferred_complete_timeline |
| `Action_RunBlock` | 152 | 155 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 158 | 182 | 25 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 119 | 91 | inferred_complete_timeline |
| `Action_None` | 203 | 210 | 8 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–108
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 84 | 56 | inferred_complete_timeline |
| `Action_None` | 89 | 108 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–183
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 158 | 130 | inferred_complete_timeline |
| `Action_None` | 160 | 183 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 210 | 182 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–73
- **Visible Samples:** 74

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 73 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–210
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 114 | 86 | inferred_complete_timeline |
| `Action_None` | 116 | 210 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–51
- **Visible Samples:** 52

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 28 | 29 | inferred_complete_timeline |
| `Action_None` | 29 | 51 | 23 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `20` | `21` | Position_Unknown | Team_Unknown | 63–103 | 41 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 68–210 | 143 | 1 | Undefined position; Undefined team |
| `23` | `36` | Position_Unknown | Team_Unknown | 151–210 | 60 | 1 | Undefined position; Undefined team |
| `24` | `41` | Position_Unknown | Team_Unknown | 157–177 | 21 | 1 | Undefined position; Undefined team |
| `25` | `44` | Position_Unknown | Team_Unknown | 161–200 | 40 | 1 | Undefined position; Undefined team |
| `26` | `45` | Position_Unknown | Team_Unknown | 169–210 | 42 | 1 | Undefined position; Undefined team |
| `27` | `46` | Position_Unknown | Team_Unknown | 176–210 | 35 | 1 | Undefined position; Undefined team |
| `28` | `47` | Position_Unknown | Team_Unknown | 197–210 | 14 | 1 | Undefined position; Undefined team |
| `29` | `48` | Position_Unknown | Team_Unknown | 199–210 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `22` | `28` | 115 | 117 | 3 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `16` (4 segments found)
- ⚠️ `Action_RunBlock` for actor_track_id `4` (C): Annotated start 35 != Inferred start 46
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `6` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `11` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `1` (actor_track_id `1`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `SAF3` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [29–45], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=46.
- ⚠️ Action 'Action_None' range [161-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-73] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [46-122] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-119] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-47] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-111] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-210] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-55] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-54] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' range [67-89] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-200] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-144] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-66] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-158] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-210] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-96] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-149] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [152-155] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [158-182] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-43] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [46-210] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-51] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [29-84] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-108] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-103] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-210] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-210] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-200] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-210] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-210] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-210] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
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

</details>