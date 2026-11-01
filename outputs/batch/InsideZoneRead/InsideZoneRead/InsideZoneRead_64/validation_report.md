# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_64`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [51–61], lower_priority='Action_ZoneBlock' annotated_start=53, effective_Action_ZoneBlock_start=62.
> - Action 'Action_None' range [51-131] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-234] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-131] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [96-145] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-77] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-149] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-90] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-113] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-155] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-201] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-83] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-62] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-99] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-90] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-214] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-173] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-158] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-191] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-208] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-239] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.