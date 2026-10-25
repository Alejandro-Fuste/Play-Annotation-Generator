# Play-Annotation-Generator Annotation Review — BootPass_68

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_68`
- **Frame Range:** 0 to 419 (420 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 419
- **Player Tracks:** 53
- **Ball Tracks:** 0
- **Action Segments:** 130
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 2
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 119
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | offense | `8` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `12` | `12` |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `8` | `8` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `15` | `15` |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | offense | `15` | `15` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `10` | `Group` | 0 | START | 5 | 20 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `12` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 5 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 5 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE3 | `16` | `Group` | 0 | START | 5 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `17` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `3` | `Group` | 0 | START | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 0 | START | 5 | 33 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Group | `8` | `Group` | 0 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `12` | `12` | 5 | START | 5 | 51 |
| ❌ MISSING SEGMENT | `Action_RunBlock` | C | `17` | `17` | 5 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LT | `3` | `3` | 5 | START | 5 | 33 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `8` | `8` | 5 | START | 5 | 69 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 34 | START | 34 | 40 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 40 | END | 34 | 40 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `15` | `15` | 50 | START | 50 | 59 |
| ❌ MISSING SEGMENT | `Action_BootAway` | QB | `15` | `15` | 78 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 5–65
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_SnapReceive` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 49 | 9 | inferred_complete_timeline |
| `Action_FakeHandoff` | 50 | 59 | 10 | inferred_complete_timeline |
| `Action_FakeHandoff` | 64 | 65 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 5–334
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 41 | 8 | inferred_complete_timeline |
| `Action_None` | 44 | 45 | 2 | inferred_complete_timeline |
| `Action_None` | 98 | 101 | 4 | inferred_complete_timeline |
| `Action_None` | 130 | 243 | 114 | inferred_complete_timeline |
| `Action_None` | 247 | 334 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 5–105
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 105 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 5–82
- **Visible Samples:** 30

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 20 | 16 | inferred_complete_timeline |
| `Action_None` | 69 | 82 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>TE3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 5–55
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 55 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 5–187
- **Visible Samples:** 135

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_RunBlock` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 46 | 51 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 58 | 66 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 73 | 78 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 103 | 187 | 85 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 5–290
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_RunBlock` | 5 | 51 | 47 | inferred_complete_timeline |
| `Action_RunBlock` | 69 | 77 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 128 | 175 | 48 | inferred_complete_timeline |
| `Action_RunBlock` | 177 | 220 | 44 | inferred_complete_timeline |
| `Action_RunBlock` | 222 | 261 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 264 | 268 | 5 | inferred_complete_timeline |
| `Action_RunBlock` | 271 | 279 | 9 | inferred_complete_timeline |
| `Action_RunBlock` | 281 | 283 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 289 | 290 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 5–192
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_None` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_BallSnap` | 34 | 40 | 7 | inferred_complete_timeline |
| `Action_None` | 41 | 107 | 67 | inferred_complete_timeline |
| `Action_None` | 114 | 192 | 79 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 5–142
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_RunBlock` | 5 | 69 | 65 | inferred_complete_timeline |
| `Action_RunBlock` | 71 | 99 | 29 | inferred_complete_timeline |
| `Action_RunBlock` | 117 | 122 | 6 | inferred_complete_timeline |
| `Action_RunBlock` | 140 | 142 | 3 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 5–76
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 76 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 5–108
- **Visible Samples:** 104

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 108 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 5–141
- **Visible Samples:** 122

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 62 | 29 | inferred_complete_timeline |
| `Action_None` | 65 | 81 | 17 | inferred_complete_timeline |
| `Action_None` | 87 | 125 | 39 | inferred_complete_timeline |
| `Action_None` | 131 | 134 | 4 | inferred_complete_timeline |
| `Action_None` | 138 | 141 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 5–172
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 117 | 84 | inferred_complete_timeline |
| `Action_None` | 121 | 172 | 52 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 5–133
- **Visible Samples:** 127

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 102 | 69 | inferred_complete_timeline |
| `Action_None` | 105 | 133 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 5–385
- **Visible Samples:** 375

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 162 | 129 | inferred_complete_timeline |
| `Action_None` | 165 | 294 | 130 | inferred_complete_timeline |
| `Action_None` | 296 | 377 | 82 | inferred_complete_timeline |
| `Action_None` | 381 | 385 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 5–210
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 117 | 84 | inferred_complete_timeline |
| `Action_None` | 121 | 210 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 5–94
- **Visible Samples:** 90

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 94 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 5–118
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 5 | 33 | 29 | inferred_complete_timeline |
| `Action_None` | 34 | 118 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `18` | Position_Unknown | Team_Unknown | 16–48 | 28 | 2 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 25–81 | 36 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 42–61 | 20 | 1 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 55–92 | 38 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 61–102 | 38 | 2 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 65–67 | 3 | 1 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 74–108 | 35 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 80–99 | 20 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 89–123 | 35 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 92–140 | 40 | 3 | Undefined position; Undefined team |
| `28` | `34` | Position_Unknown | Team_Unknown | 105–127 | 23 | 1 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 111–138 | 23 | 3 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 111–162 | 52 | 1 | Undefined position; Undefined team |
| `31` | `37` | Position_Unknown | Team_Unknown | 125–128 | 4 | 1 | Undefined position; Undefined team |
| `32` | `38` | Position_Unknown | Team_Unknown | 126–256 | 126 | 2 | Undefined position; Undefined team |
| `33` | `41` | Position_Unknown | Team_Unknown | 140–273 | 134 | 1 | Undefined position; Undefined team |
| `34` | `47` | Position_Unknown | Team_Unknown | 143–148 | 6 | 1 | Undefined position; Undefined team |
| `35` | `48` | Position_Unknown | Team_Unknown | 144–300 | 152 | 2 | Undefined position; Undefined team |
| `36` | `51` | Position_Unknown | Team_Unknown | 145–153 | 9 | 1 | Undefined position; Undefined team |
| `37` | `52` | Position_Unknown | Team_Unknown | 146–409 | 262 | 2 | Undefined position; Undefined team |
| `38` | `54` | Position_Unknown | Team_Unknown | 161–167 | 7 | 1 | Undefined position; Undefined team |
| `39` | `55` | Position_Unknown | Team_Unknown | 163–419 | 257 | 1 | Undefined position; Undefined team |
| `40` | `56` | Position_Unknown | Team_Unknown | 171–172 | 2 | 1 | Undefined position; Undefined team |
| `41` | `57` | Position_Unknown | Team_Unknown | 179–338 | 121 | 8 | Undefined position; Undefined team |
| `42` | `61` | Position_Unknown | Team_Unknown | 189–199 | 4 | 2 | Undefined position; Undefined team |
| `43` | `64` | Position_Unknown | Team_Unknown | 284–294 | 11 | 1 | Undefined position; Undefined team |
| `44` | `65` | Position_Unknown | Team_Unknown | 292–325 | 28 | 4 | Undefined position; Undefined team |
| `45` | `67` | Position_Unknown | Team_Unknown | 296–419 | 123 | 2 | Undefined position; Undefined team |
| `46` | `68` | Position_Unknown | Team_Unknown | 303–419 | 117 | 1 | Undefined position; Undefined team |
| `47` | `69` | Position_Unknown | Team_Unknown | 312–419 | 108 | 1 | Undefined position; Undefined team |
| `48` | `70` | Position_Unknown | Team_Unknown | 337–419 | 83 | 1 | Undefined position; Undefined team |
| `49` | `72` | Position_Unknown | Team_Unknown | 368–419 | 52 | 1 | Undefined position; Undefined team |
| `50` | `74` | Position_Unknown | Team_Unknown | 390–395 | 6 | 1 | Undefined position; Undefined team |
| `51` | `75` | Position_Unknown | Team_Unknown | 396–419 | 21 | 3 | Undefined position; Undefined team |
| `52` | `77` | Position_Unknown | Team_Unknown | 415–419 | 5 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `12` (9 segments found)
- ❌ Missing segment for action `Action_RunBlock` on target `17` (C)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `3` (5 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `8` (4 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `15` (2 segments found)
- ❌ Missing segment for action `Action_BootAway` on target `15` (QB)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `SAF2` position mapped to `defense` team
- ⚠️ 35 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 35 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 70 |
| Missing visible bounding boxes during action | 108 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
- ⚠️ Segment 'Action_BootAway' for track '15' has invalid range: start=78, end=65. Clamping end to start.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [34–40], lower_priority='Action_RunBlock' annotated_start=5, effective_Action_RunBlock_start=41.
- ⚠️ Action 'Action_None' range [34-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-133] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-162] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-294] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-377] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [381-385] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-76] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [5-33] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [46-51] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [58-66] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [73-78] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [103-187] for track '3' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-108] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-94] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-105] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-172] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [5-69] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [71-99] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [117-122] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [140-142] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [5-20] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [69-82] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-117] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-210] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [5-51] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [69-77] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [128-175] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [177-220] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [222-261] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [264-268] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [271-279] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [281-283] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [289-290] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-62] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-81] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [87-125] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-134] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-141] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-101] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-243] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [247-334] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_SnapReceive' range [34-40] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [50-59] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [64-65] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-55] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-107] for track '17' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-192] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [16-31] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [37-48] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-33] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [34-37] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [45-51] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-61] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-70] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-81] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [42-61] for track '20' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [55-92] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-74] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [79-102] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [65-67] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-108] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-99] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-123] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-117] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-130] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-140] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [105-127] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-118] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-123] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [128-138] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-128] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-202] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-256] for track '32' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-273] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [143-148] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [144-286] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-300] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-153] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-200] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-409] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-167] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-419] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-172] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-192] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-206] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [219-221] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-233] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-323] for track '41' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [333-338] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-199] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [284-294] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-298] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [300-315] for track '44' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-318] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [323-325] for track '44' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [296-328] for track '45' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [390-395] for track '50' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [396-399] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [402-404] for track '51' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [406-419] for track '51' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '45' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '45' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '46' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '46' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '47' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '47' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '48' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '48' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '49' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '49' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '50' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '50' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '51' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '51' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '52' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '52' has undefined team_side. Will map to Team_Unknown.

</details>