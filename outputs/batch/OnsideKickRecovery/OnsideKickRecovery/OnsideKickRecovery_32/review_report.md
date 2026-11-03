# Play-Annotation-Generator Annotation Review — OnsideKickRecovery_32

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `OnsideKickRecovery_32`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_SpecialTeams_OnsideKickRecovery`
- **Result:** `Result_Unknown`
- **Result Frame:** 239
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 55
- **Validation Warnings:** 43
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 2
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 42
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | offense | `9` | `Group` |
| ✅ EXACT | `Action_KickApproach` | Kicker | offense | `9` | `9` |
| ✅ EXACT | `Action_KickBall` | Kicker | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Kicker | offense | `9` | `9` |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | offense | `9` | `9` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage6 | `0` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage5 | `10` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage4 | `12` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage4 | `14` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage2 | `15` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage2 | `16` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage1 | `17` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage1 | `18` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Right_Coverage3 | `4` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Left_Coverage3 | `7` | `Group` | 0 | START | 0 | 1 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | Kicker | `9` | `Group` | 0 | START | 0 | 1 |
| ✅ EXACT | `Action_KickApproach` | Kicker | `9` | `9` | 2 | START | 2 | 37 |
| ✅ EXACT | `Action_KickBall` | Kicker | `9` | `9` | 38 | START | 38 | 82 |
| ❌ MISSING SEGMENT | `Action_AttemptRecovery` | Kicker | `9` | `9` | 85 | START | N/A | N/A |
| ❌ MISSING SEGMENT | `Action_SecureRecovery` | Kicker | `9` | `9` | 102 | START | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>Kicker — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–82
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_KickApproach` | 2 | 37 | 36 | inferred_complete_timeline |
| `Action_KickBall` | 38 | 82 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage1 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 34 | 33 | inferred_complete_timeline |
| `Action_None` | 36 | 110 | 75 | inferred_complete_timeline |
| `Action_None` | 113 | 120 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>Left_Coverage4 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage4 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage5 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Right_Coverage6 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 102 | 101 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>Kick_Returner — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 23 | 22 | inferred_complete_timeline |
| `Action_None` | 74 | 83 | 10 | inferred_complete_timeline |
| `Action_None` | 89 | 119 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 90 | 89 | inferred_complete_timeline |
| `Action_None` | 97 | 120 | 24 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front5 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Front6 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support3 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 120 | 119 | inferred_complete_timeline |

</details>

<details>
<summary>Onside_Recovery_Support4 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 120

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 1 | 2 | inferred_complete_timeline |
| `Action_None` | 2 | 119 | 118 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 48–80 | 13 | 2 | Undefined position; Undefined team |
| `23` | `28` | Position_Unknown | Team_Unknown | 91–92 | 2 | 1 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 107–120 | 14 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 112–113 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_AttemptRecovery` on target `9` (Kicker)
- ❌ Missing segment for action `Action_SecureRecovery` on target `9` (Kicker)

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `Right_Coverage6` position mapped to `offense` team
- ⚠️ Player track XML ID `1` (actor_track_id `1`): `Onside_Recovery_Support4` position mapped to `defense` team
- ⚠️ Player track XML ID `2` (actor_track_id `2`): `Onside_Recovery_Front2` position mapped to `defense` team
- ⚠️ Player track XML ID `3` (actor_track_id `3`): `Onside_Recovery_Front1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `Right_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `5` (actor_track_id `5`): `Onside_Recovery_Front4` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `Onside_Recovery_Front6` position mapped to `defense` team
- ⚠️ Player track XML ID `7` (actor_track_id `7`): `Left_Coverage3` position mapped to `offense` team
- ⚠️ Player track XML ID `8` (actor_track_id `8`): `Onside_Recovery_Support3` position mapped to `defense` team
- ⚠️ Player track XML ID `9` (actor_track_id `9`): `Kicker` position mapped to `offense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `Right_Coverage5` position mapped to `offense` team
- ⚠️ Player track XML ID `11` (actor_track_id `11`): `Onside_Recovery_Front5` position mapped to `defense` team
- ⚠️ Player track XML ID `12` (actor_track_id `12`): `Right_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `Onside_Recovery_Front3` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `Left_Coverage4` position mapped to `offense` team
- ⚠️ Player track XML ID `15` (actor_track_id `15`): `Left_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `16` (actor_track_id `16`): `Right_Coverage2` position mapped to `offense` team
- ⚠️ Player track XML ID `17` (actor_track_id `17`): `Right_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `18` (actor_track_id `18`): `Left_Coverage1` position mapped to `offense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `Onside_Recovery_Support1` position mapped to `defense` team
- ⚠️ Player track XML ID `20` (actor_track_id `20`): `Onside_Recovery_Support2` position mapped to `defense` team
- ⚠️ Player track XML ID `21` (actor_track_id `21`): `Kick_Returner` position mapped to `defense` team
- ⚠️ 4 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 4 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 8 |
| Missing visible bounding boxes during action | 32 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_AttemptRecovery' for track '9' has invalid range: start=85, end=82. Clamping end to start.
- ⚠️ Segment 'Action_SecureRecovery' for track '9' has invalid range: start=102, end=82. Clamping end to start.
- ⚠️ Action 'Action_None' range [2-102] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-119] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-90] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-120] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-34] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [36-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-120] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_KickBall' range [38-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '19' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-120] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [2-23] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-83] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-119] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [48-55] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [76-80] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-92] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-120] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-113] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>