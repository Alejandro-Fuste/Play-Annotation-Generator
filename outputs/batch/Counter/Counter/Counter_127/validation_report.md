# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_127`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [37-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-203] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-123] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-101] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-117] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-133] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-141] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-186] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-111] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [87-167] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-170] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-168] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-205] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [39-85] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-155] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-175] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [39-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-210] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [37-88] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [37-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [58-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [39-104] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-198] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.