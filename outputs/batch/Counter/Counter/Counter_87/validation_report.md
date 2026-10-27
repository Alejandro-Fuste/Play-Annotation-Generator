# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_87`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_87/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 61 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '2' (C) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
> - Validation warning: Action 'Action_PullBlock' for track '19' (RT) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 95 frames exceeds threshold 90 frames [start=65, end=159].
> - Action 'Action_None' range [63-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-93] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [111-159] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [111-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-109] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-141] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-135] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [71-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [65-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-180] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-178] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.