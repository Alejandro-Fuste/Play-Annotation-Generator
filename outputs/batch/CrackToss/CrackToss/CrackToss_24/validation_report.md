# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_24`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_24/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 44 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 358 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 358 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '13' (LT) duration 93 frames exceeds threshold 90 frames [start=129, end=221].
> - Action 'Action_PreSnap' range [0-4] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-219] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_Toss' range [148-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [129-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-152] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-198] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-230] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-327] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-357] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-173] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [129-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [173-209] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-264] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-232] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [165-253] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-198] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-343] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-223] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-244] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-262] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-256] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-277] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-154] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-358] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-358] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-149] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-158] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-190] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-73] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-164] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-172] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-234] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-326] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-330] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-221] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-207] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-271] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-281] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-358] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [257-336] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-333] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-339] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-316] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-340] for track '39' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.