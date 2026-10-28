# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_58`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_58/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [77–88], lower_priority='Action_PassBlock' annotated_start=80, effective_Action_PassBlock_start=89.
> - Action 'Action_None' range [77-164] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-164] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-110] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-42] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-182] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [116-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-104] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-53] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-60] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-116] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [122-139] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-125] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-19] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-37] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-47] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-67] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-135] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-142] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-167] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-256] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [127-161] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-243] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-208] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-254] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-261] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-269] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-269] for track '32' has 3 frames without a visible bounding box.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.