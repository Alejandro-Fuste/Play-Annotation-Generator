# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_23`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [32–47], lower_priority='Action_PassBlock' annotated_start=35, effective_Action_PassBlock_start=48.
> - Action 'Action_None' range [32-158] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-140] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-196] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [32-83] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-149] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [74-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-239] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [32-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-124] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-131] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-223] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-63] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-215] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [48-99] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-170] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-68] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-100] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-83] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-239] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-219] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-216] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-199] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-215] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.