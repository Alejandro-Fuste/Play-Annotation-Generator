# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_11`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 14: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PreSnap' range [0-47] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-63] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-152] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [6-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [151-153] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [155-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [182-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [189-190] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [192-204] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-228] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-236] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-99] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-148] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-167] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-182] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-238] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-239] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [167-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-126] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-165] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-149] for track '18' has 8 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [157-158] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-66] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [3-164] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-145] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-54] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-153] for track '24' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-159] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-144] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-169] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-201] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-216] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-203] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-238] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-234] for track '31' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '8' has undefined position. Will map to Position_Unknown.
> - Player track '8' has undefined team_side. Will map to Team_Unknown.
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