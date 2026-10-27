# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_8`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_8/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '1' (LG) duration 91 frames exceeds threshold 90 frames [start=86, end=176].
> - Validation warning: Action 'Action_DownBlock' for track '7' (RG) duration 91 frames exceeds threshold 90 frames [start=86, end=176].
> - Segment 'Action_BallSnap' for track '15' has invalid range: start=88, end=86. Clamping end to start.
> - Action 'Action_PlaySideFakeStep' range [86-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PlaySideFakeStep' range [177-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-131] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [154-176] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 177, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [177-177] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-204] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-108] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [86-116] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [130-167] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-141] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-188] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [117-170] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-152] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-177] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-142] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [86-107] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-13] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-32] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-48] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-145] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [88-143] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [149-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-256] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-126] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-202] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-166] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-193] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-207] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '32' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.