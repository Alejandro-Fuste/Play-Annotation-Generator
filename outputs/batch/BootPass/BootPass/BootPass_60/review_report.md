# Play-Annotation-Generator Annotation Review — BootPass_60

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_60`
- **Frame Range:** 0 to 389 (390 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 389
- **Player Tracks:** 47
- **Ball Tracks:** 0
- **Action Segments:** 108
- **Validation Warnings:** 142
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 7
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 88
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `9` | `Group` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | Team_Unknown | `17` | `16` |
| ✅ EXACT | `Action_RunBlock` | RG | offense | `0` | `0` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `3` | `3` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `4` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_RunFlatRoute` | TE1 | offense | `2` | `2` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `15` | `15` |
| ✅ EXACT | `Action_SecureCatch` | TE1 | offense | `2` | `2` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `0` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `1` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `13` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `15` | `Group` | 0 | START | 0 | 49 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `2` | `Group` | 0 | START | 0 | 61 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 0 | START | 0 | 56 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `9` | `Group` | 0 | START | 0 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallSnap` | Position_Unknown | `17` | `16` | 50 | START | 50 | 60 |
| ✅ EXACT | `Action_RunBlock` | RG | `0` | `0` | 57 | START | 57 | 87 |
| ✅ EXACT | `Action_RunBlock` | RT | `3` | `3` | 57 | START | 57 | 167 |
| ✅ EXACT | `Action_RunBlock` | LT | `4` | `4` | 57 | START | 57 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `9` | `9` | 57 | START | 57 | 118 |
| ✅ EXACT | `Action_SnapReceive` | QB | `15` | `15` | 65 | END | 50 | 65 |
| ⚠️ AMBIGUOUS MATCH | `Action_FakeHandoff` | QB | `15` | `15` | 74 | START | 74 | 75 |
| ⚠️ AMBIGUOUS MATCH | `Action_BootAway` | QB | `15` | `15` | 88 | START | 88 | 92 |
| ✅ EXACT | `Action_RunFlatRoute` | TE1 | `2` | `2` | 97 | START | 97 | 135 |
| ✅ EXACT | `Action_ThrowPass` | QB | `15` | `15` | 135 | START | 135 | 146 |
| ✅ EXACT | `Action_SecureCatch` | TE1 | `2` | `2` | 214 | START | 214 | 221 |

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
- **Visible Frames:** 0–389
- **Visible Samples:** 376

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_SnapReceive` | 50 | 65 | 16 | inferred_complete_timeline |
| `Action_None` | 66 | 73 | 8 | inferred_complete_timeline |
| `Action_FakeHandoff` | 74 | 75 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 85 | 87 | 3 | inferred_complete_timeline |
| `Action_BootAway` | 88 | 92 | 5 | inferred_complete_timeline |
| `Action_BootAway` | 98 | 125 | 28 | inferred_complete_timeline |
| `Action_None` | 126 | 134 | 9 | inferred_complete_timeline |
| `Action_ThrowPass` | 135 | 146 | 12 | inferred_complete_timeline |
| `Action_None` | 147 | 389 | 243 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 136 | 87 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–359
- **Visible Samples:** 313

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 61 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 96 | 29 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 97 | 135 | 39 | inferred_complete_timeline |
| `Action_None` | 136 | 171 | 36 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_SecureCatch` | 214 | 221 | 8 | inferred_complete_timeline |
| `Action_None` | 222 | 238 | 17 | inferred_complete_timeline |
| `Action_None` | 241 | 359 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 173 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–128
- **Visible Samples:** 129

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 128 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–144
- **Visible Samples:** 143

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 118 | 62 | inferred_complete_timeline |
| `Action_RunBlock` | 121 | 144 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–87
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 87 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_RunBlock` | 57 | 167 | 111 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 67 | 18 | inferred_complete_timeline |
| `Action_None` | 91 | 95 | 5 | inferred_complete_timeline |
| `Action_None` | 136 | 164 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 167 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–58
- **Visible Samples:** 59

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 58 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–103
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 79 | 30 | inferred_complete_timeline |
| `Action_None` | 84 | 103 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–136
- **Visible Samples:** 126

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 120 | 71 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–339
- **Visible Samples:** 331

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 167 | 118 | inferred_complete_timeline |
| `Action_None` | 176 | 197 | 22 | inferred_complete_timeline |
| `Action_None` | 199 | 339 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–114
- **Visible Samples:** 102

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 99 | 50 | inferred_complete_timeline |
| `Action_None` | 113 | 114 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–389
- **Visible Samples:** 366

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_None` | 50 | 167 | 118 | inferred_complete_timeline |
| `Action_None` | 173 | 190 | 18 | inferred_complete_timeline |
| `Action_None` | 203 | 343 | 141 | inferred_complete_timeline |
| `Action_None` | 351 | 389 | 39 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 18–153 | 118 | 6 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 72–132 | 61 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 81–117 | 37 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 90–171 | 82 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 96–102 | 7 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 106–111 | 6 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 108–389 | 262 | 3 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 111–136 | 26 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 111–112 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 114–163 | 50 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 118–148 | 31 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 150–389 | 215 | 5 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 154–332 | 135 | 4 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 157–166 | 10 | 1 | Undefined position; Undefined team |
| `30` | `34` | Position_Unknown | Team_Unknown | 161–162 | 2 | 1 | Undefined position; Undefined team |
| `31` | `35` | Position_Unknown | Team_Unknown | 168–222 | 52 | 2 | Undefined position; Undefined team |
| `32` | `36` | Position_Unknown | Team_Unknown | 168–173 | 6 | 1 | Undefined position; Undefined team |
| `33` | `38` | Position_Unknown | Team_Unknown | 168–188 | 21 | 1 | Undefined position; Undefined team |
| `34` | `39` | Position_Unknown | Team_Unknown | 171–177 | 7 | 1 | Undefined position; Undefined team |
| `35` | `40` | Position_Unknown | Team_Unknown | 172–173 | 2 | 1 | Undefined position; Undefined team |
| `36` | `41` | Position_Unknown | Team_Unknown | 172–203 | 32 | 1 | Undefined position; Undefined team |
| `37` | `42` | Position_Unknown | Team_Unknown | 174–389 | 184 | 4 | Undefined position; Undefined team |
| `38` | `44` | Position_Unknown | Team_Unknown | 181–256 | 76 | 1 | Undefined position; Undefined team |
| `39` | `45` | Position_Unknown | Team_Unknown | 260–265 | 6 | 1 | Undefined position; Undefined team |
| `40` | `46` | Position_Unknown | Team_Unknown | 267–344 | 78 | 1 | Undefined position; Undefined team |
| `41` | `47` | Position_Unknown | Team_Unknown | 273–312 | 31 | 3 | Undefined position; Undefined team |
| `42` | `49` | Position_Unknown | Team_Unknown | 291–296 | 6 | 1 | Undefined position; Undefined team |
| `43` | `52` | Position_Unknown | Team_Unknown | 376–389 | 14 | 1 | Undefined position; Undefined team |
| `44` | `53` | Position_Unknown | Team_Unknown | 379–380 | 2 | 1 | Undefined position; Undefined team |
| `45` | `55` | Position_Unknown | Team_Unknown | 384–389 | 6 | 1 | Undefined position; Undefined team |
| `46` | `56` | Position_Unknown | Team_Unknown | 388–389 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_BallSnap` and target `17` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `9` (2 segments found)
- ⚠️ Ambiguous match for action `Action_FakeHandoff` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BootAway` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ 31 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 31 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 62 |
| Missing visible bounding boxes during action | 79 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
- ⚠️ Action 'Action_RunBlock' range [57-87] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-173] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-61] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-171] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-238] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-359] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-167] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-128] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-67] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-95] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-164] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-167] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-190] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-343] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-389] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-99] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-167] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-197] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-339] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [57-118] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [121-144] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-79] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [84-103] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-167] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-136] for track '13' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [50-58] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [74-75] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_FakeHandoff' range [85-87] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BootAway' for track '15' starts at frame 88, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_BootAway' range [88-92] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [18-21] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [33-40] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-49] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [50-60] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [62-63] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-153] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-132] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [81-117] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-102] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [106-111] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [108-113] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-359] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-136] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-112] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-163] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-148] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-152] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-310] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [317-348] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-360] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [364-389] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-284] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-296] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [330-332] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-162] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-210] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-222] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-188] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-177] for track '34' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-173] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-203] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [174-250] for track '37' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-348] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [351-359] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-256] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-344] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [273-277] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-290] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-312] for track '41' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [291-296] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [379-380] for track '44' has 1 frames without a visible bounding box.
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

</details>