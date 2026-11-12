# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_102`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_102/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 39 |
| Ball Tracks | 6 |
| CSV events parsed | 19 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 206: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LT) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
> - Validation warning: Action 'Action_ZoneBlock' for track '7' (RG) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
> - Validation warning: Action 'Action_ZoneBlock' for track '10' (C) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [490–504], lower_priority='Action_ZoneBlock' annotated_start=493, effective_Action_ZoneBlock_start=505.
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (LG) duration 118 frames exceeds threshold 90 frames [start=493, end=610].
> - Action 'Action_SplitBlock' range [498-522] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [579-592] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [493-514] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [516-517] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-546] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-631] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [490-689] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [493-568] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [611-622] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-635] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-652] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [519-529] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [573-574] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [576-582] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [505-586] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [589-610] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [611-624] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-628] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [493-583] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [586-589] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [611-627] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [519-530] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [532-546] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-489] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-517] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [490-655] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-173] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-201] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-305] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-220] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-227] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [456-457] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [477-480] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [486-489] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '22' starts at frame 490, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [490-492] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [497-570] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [572-674] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [523-529] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [528-548] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [537-540] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [550-579] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [540-689] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [543-583] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [601-657] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [546-561] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [566-607] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-587] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [589-601] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [563-587] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-666] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [591-633] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [637-647] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [591-641] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [595-597] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [599-601] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [603-644] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [608-640] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [614-618] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [620-623] for track '39' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.