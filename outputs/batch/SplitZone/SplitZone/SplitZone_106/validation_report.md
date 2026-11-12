# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_106`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [58–69], lower_priority='Action_ZoneBlock' annotated_start=61, effective_Action_ZoneBlock_start=70.
> - Action 'Action_None' range [58-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-92] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-104] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [82-106] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [125-131] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [64-87] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [102-103] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-122] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-163] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-132] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-157] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-223] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-168] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-228] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-201] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-145] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-226] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-234] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-219] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-236] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '34' has 1 frames without a visible bounding box.
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