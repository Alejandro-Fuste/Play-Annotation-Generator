# Play-Annotation-Generator Annotation Review — BootPass_117

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_117`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 76
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 7
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 3
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 56
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `14` | `14` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LT | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_FakeHandoff` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_BootAway` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_RunFlatRoute` | SAF2 | defense | `11` | `11` |
| ✅ EXACT | `Action_ThrowPass` | LT | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | SAF2 | defense | `11` | `11` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `10` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `15` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `17` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `19` | `Group` | 0 | START | 0 | 18 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `20` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `8` | `Group` | 0 | START | 0 | 40 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 40 |
| ✅ EXACT | `Action_RunBlock` | RT | `14` | `14` | 19 | START | 19 | 183 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | LT | `15` | `15` | 19 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `16` | `16` | 19 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `17` | `17` | 19 | START | 19 | 90 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `19` | `19` | 19 | START | 19 | 62 |
| ❌ MISSING SEGMENT | `Action_SnapReceive` | LT | `15` | `15` | 19 | END | N/A | N/A |
| ✅ EXACT | `Action_FakeHandoff` | LT | `15` | `15` | 31 | START | 31 | 46 |
| ✅ EXACT | `Action_BallSnap` | C | `16` | `16` | 41 | START | 41 | 41 |
| ✅ EXACT | `Action_BootAway` | LT | `15` | `15` | 47 | START | 47 | 65 |
| ✅ EXACT | `Action_RunFlatRoute` | SAF2 | `11` | `11` | 54 | START | 54 | 93 |
| ✅ EXACT | `Action_ThrowPass` | LT | `15` | `15` | 71 | START | 71 | 80 |
| ✅ EXACT | `Action_SecureCatch` | SAF2 | `11` | `11` | 94 | START | 94 | 109 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–154
- **Visible Samples:** 155

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 154 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 220 | 180 | inferred_complete_timeline |
| `Action_None` | 222 | 235 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–201
- **Visible Samples:** 202

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 201 | 161 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_FakeHandoff` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_BootAway` | 47 | 65 | 19 | inferred_complete_timeline |
| `Action_None` | 66 | 70 | 5 | inferred_complete_timeline |
| `Action_ThrowPass` | 71 | 80 | 10 | inferred_complete_timeline |
| `Action_None` | 81 | 102 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–175
- **Visible Samples:** 170

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 19 | 90 | 72 | inferred_complete_timeline |
| `Action_RunBlock` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 96 | 97 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 101 | 175 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–77
- **Visible Samples:** 76

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_None` | 19 | 40 | 22 | inferred_complete_timeline |
| `Action_BallSnap` | 41 | 41 | 1 | inferred_complete_timeline |
| `Action_None` | 42 | 73 | 32 | inferred_complete_timeline |
| `Action_None` | 76 | 77 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–171
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 19 | 62 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 68 | 75 | 8 | inferred_complete_timeline |
| `Action_RunBlock` | 81 | 171 | 91 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 184

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 18 | 19 | inferred_complete_timeline |
| `Action_RunBlock` | 19 | 183 | 165 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 82 | 42 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 159

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 13 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 15 | 40 | 26 | inferred_complete_timeline |
| `Action_None` | 41 | 69 | 29 | inferred_complete_timeline |
| `Action_None` | 71 | 160 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–182
- **Visible Samples:** 183

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 182 | 142 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–185
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 82 | 42 | inferred_complete_timeline |
| `Action_None` | 88 | 185 | 98 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 118 | 78 | inferred_complete_timeline |
| `Action_None` | 121 | 239 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 100 | 60 | inferred_complete_timeline |
| `Action_None` | 104 | 107 | 4 | inferred_complete_timeline |
| `Action_None` | 109 | 123 | 15 | inferred_complete_timeline |
| `Action_None` | 125 | 239 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 40 | 41 | inferred_complete_timeline |
| `Action_None` | 41 | 227 | 187 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 53 | 54 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 54 | 93 | 40 | inferred_complete_timeline |
| `Action_SecureCatch` | 94 | 109 | 16 | inferred_complete_timeline |
| `Action_None` | 110 | 239 | 130 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `26` | Position_Unknown | Team_Unknown | 79–181 | 94 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 94–95 | 2 | 1 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 112–239 | 123 | 4 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 116–162 | 47 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 121–125 | 5 | 1 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 135–137 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_RunBlock` on target `15` (LT)
- ❌ Missing segment for action `Action_RunBlock` on target `16` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `19` (3 segments found)
- ❌ Missing segment for action `Action_SnapReceive` on target `15` (LT)

### Track Identity Issues

- ⚠️ Player track XML ID `11` (actor_track_id `11`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 40 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Overlapping action conflict at frame 19 for track '15': 'Action_RunBlock' vs 'Action_SnapReceive'. Overriding with 'Action_SnapReceive'.
- ⚠️ Segment 'Action_SnapReceive' for track '15' has invalid range: start=41, end=19. Clamping end to start.
- ⚠️ Segment 'Action_BallSnap' for track '16' has invalid range: start=41, end=19. Clamping end to start.
- ⚠️ Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [41–41], lower_priority='Action_RunBlock' annotated_start=19, effective_Action_RunBlock_start=42.
- ⚠️ Action 'Action_None' range [41-82] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-182] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-100] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-107] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [109-123] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-220] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-235] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-201] for track '9' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-239] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-227] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-82] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [88-185] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [19-183] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-102] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-77] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [19-90] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [92-93] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [96-97] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [101-175] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-118] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [19-62] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [68-75] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [81-171] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-154] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-13] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-69] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-160] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-89] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-181] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-118] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-157] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-162] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-125] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '27' has 1 frames without a visible bounding box.
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

</details>