# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_170`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_170/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '9' has invalid range: start=121, end=99. Clamping end to start.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [68–84], lower_priority='Action_ZoneBlock' annotated_start=71, effective_Action_ZoneBlock_start=85.
> - Action 'Action_None' range [68-181] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-232] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-299] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-229] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-152] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-247] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-197] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-107] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-209] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 101, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [101-101] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-247] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-264] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [186-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [76-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [80-82] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [84-91] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-258] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-82] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-114] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-282] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-147] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-272] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-139] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-233] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-169] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-195] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-267] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '25' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.