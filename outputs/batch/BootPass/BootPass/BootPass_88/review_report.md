# Play-Annotation-Generator Annotation Review — BootPass_88

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_88`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 69
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 9
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 61
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `7` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `18` | `18` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `2` | `2` |
| ✅ EXACT | `Action_RunBlock` | RT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | offense | `7` | `7` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_RunFlatRoute` | DE2 | defense | `13` | `13` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `17` | `17` |
| ✅ EXACT | `Action_SecureCatch` | SAF2 | defense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `0` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `10` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `16` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `17` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `2` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `3` | `Group` | 0 | START | 0 | 34 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `7` | `Group` | 0 | START | 0 | 34 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 27 | START | 27 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `15` | `15` | 35 | START | 35 | 130 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `18` | `18` | 35 | START | 43 | 59 |
| ✅ EXACT | `Action_RunBlock` | LT | `2` | `2` | 35 | START | 35 | 129 |
| ✅ EXACT | `Action_RunBlock` | RT | `3` | `3` | 35 | START | 35 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | LG | `7` | `7` | 35 | START | 35 | 48 |
| ✅ EXACT | `Action_SnapReceive` | QB | `17` | `17` | 42 | END | 27 | 42 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `17` | `17` | 47 | START | 47 | 68 |
| ✅ EXACT | `Action_BootAway` | QB | `17` | `17` | 69 | START | 69 | 115 |
| ✅ EXACT | `Action_RunFlatRoute` | DE2 | `13` | `13` | 69 | START | 69 | 116 |
| ✅ EXACT | `Action_ThrowPass` | QB | `17` | `17` | 116 | START | 116 | 123 |
| ✅ EXACT | `Action_SecureCatch` | SAF2 | `8` | `8` | 144 | START | 144 | 155 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 174

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 46 | 4 | inferred_complete_timeline |
| `Action_FakeHandoff` | 47 | 68 | 22 | inferred_complete_timeline |
| `Action_BootAway` | 69 | 115 | 47 | inferred_complete_timeline |
| `Action_ThrowPass` | 116 | 123 | 8 | inferred_complete_timeline |
| `Action_None` | 124 | 173 | 50 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 63 | 37 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–134
- **Visible Samples:** 128

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 56 | 30 | inferred_complete_timeline |
| `Action_None` | 60 | 106 | 47 | inferred_complete_timeline |
| `Action_None` | 110 | 118 | 9 | inferred_complete_timeline |
| `Action_None` | 120 | 134 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–69
- **Visible Samples:** 70

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 69 | 43 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–167
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 167 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–129
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 129 | 95 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–165
- **Visible Samples:** 151

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 48 | 14 | inferred_complete_timeline |
| `Action_RunBlock` | 50 | 131 | 82 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 135 | 2 | inferred_complete_timeline |
| `Action_RunBlock` | 148 | 165 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_BallSnap` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 43 | 59 | 17 | inferred_complete_timeline |
| `Action_RunBlock` | 80 | 239 | 160 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–173
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 130 | 96 | inferred_complete_timeline |
| `Action_RunBlock` | 134 | 173 | 40 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 182

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 34 | 35 | inferred_complete_timeline |
| `Action_RunBlock` | 35 | 181 | 147 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–238
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 19 | 20 | inferred_complete_timeline |
| `Action_PreSnap` | 26 | 26 | 1 | inferred_complete_timeline |
| `Action_None` | 27 | 31 | 5 | inferred_complete_timeline |
| `Action_None` | 36 | 62 | 27 | inferred_complete_timeline |
| `Action_None` | 64 | 121 | 58 | inferred_complete_timeline |
| `Action_None` | 125 | 238 | 114 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 68 | 69 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 69 | 116 | 48 | inferred_complete_timeline |
| `Action_None` | 117 | 239 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 38

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 35 | 9 | inferred_complete_timeline |
| `Action_None` | 63 | 64 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–66
- **Visible Samples:** 64

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 37 | 11 | inferred_complete_timeline |
| `Action_None` | 41 | 66 | 26 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–161
- **Visible Samples:** 130

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 80 | 54 | inferred_complete_timeline |
| `Action_None` | 113 | 161 | 49 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–116
- **Visible Samples:** 117

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 116 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 239 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 225

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 224 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 111 | 112 | inferred_complete_timeline |
| `Action_PreSnap` | 116 | 118 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 143 | 24 | inferred_complete_timeline |
| `Action_SecureCatch` | 144 | 155 | 12 | inferred_complete_timeline |
| `Action_None` | 156 | 239 | 84 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `9` | `9` | Position_Unknown | Team_Unknown | 0–74 | 68 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 40–107 | 50 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 58–176 | 118 | 2 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 67–131 | 65 | 1 | Undefined position; Undefined team |
| `25` | `26` | Position_Unknown | Team_Unknown | 72–117 | 46 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 125–234 | 110 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 133–148 | 16 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 138–176 | 31 | 4 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 172–174 | 3 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `15` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `8` (actor_track_id `8`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 9 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 9 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 18 |
| Missing visible bounding boxes during action | 49 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [27–42], lower_priority='Action_RunBlock' annotated_start=35, effective_Action_RunBlock_start=43.
- ⚠️ Action 'Action_None' range [27-167] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-80] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-161] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-129] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-116] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-48] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [50-131] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-135] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [148-165] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-111] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [116-118] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [156-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-47] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-50] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-74] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-63] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-56] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-106] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [110-118] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [120-134] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-224] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [35-130] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [134-173] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-69] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [124-173] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [43-59] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-35] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-37] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-66] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-31] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-62] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-121] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-238] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-47] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [66-107] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [58-60] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [62-176] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [67-131] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [72-117] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-234] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-148] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-154] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-176] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Player track '9' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '9' has undefined team_side. Will map to Team_Unknown.
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

</details>