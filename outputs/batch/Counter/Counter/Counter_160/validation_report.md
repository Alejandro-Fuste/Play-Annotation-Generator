# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_160`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_160/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '17' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '16' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '23' in Player Track ID sheet does not exist in MOT gt.txt.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '4' (SAF1) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
> - Validation warning: Action 'Action_DownBlock' for track '5' (CB2) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
> - Validation warning: Action 'Action_DownBlock' for track '10' (TE) duration 97 frames exceeds threshold 90 frames [start=55, end=151].
> - Action 'Action_PullBlock' range [55-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [58-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [100-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [55-151] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-93] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-203] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-46] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [55-151] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-160] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-194] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-167] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-207] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.