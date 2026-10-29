# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_43`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 80 |
| Player Tracks | 80 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 159 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [22–36], lower_priority='Action_PassBlock' annotated_start=25, effective_Action_PassBlock_start=37.
> - Action 'Action_None' range [22-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-53] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-91] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-180] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [36-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [80-165] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunDeepCrossRoute' range [167-171] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-64] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-178] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-65] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-151] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-174] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-80] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-105] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-76] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-169] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-139] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-159] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-178] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [128-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [161-174] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [176-177] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-178] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [37-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [25-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [183-185] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-148] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-111] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-178] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-84] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-96] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-199] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [86-96] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-178] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-114] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-122] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '48' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '49' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '52' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '53' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '54' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '55' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '56' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '57' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '58' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '59' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-201] for track '60' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '61' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '62' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '63' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '64' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '65' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-188] for track '66' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '67' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '68' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '69' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '70' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '71' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '72' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '73' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '74' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '75' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-206] for track '76' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '77' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '78' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '79' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.
> - Player track '53' has undefined position. Will map to Position_Unknown.
> - Player track '53' has undefined team_side. Will map to Team_Unknown.
> - Player track '54' has undefined position. Will map to Position_Unknown.
> - Player track '54' has undefined team_side. Will map to Team_Unknown.
> - Player track '55' has undefined position. Will map to Position_Unknown.
> - Player track '55' has undefined team_side. Will map to Team_Unknown.
> - Player track '56' has undefined position. Will map to Position_Unknown.
> - Player track '56' has undefined team_side. Will map to Team_Unknown.
> - Player track '57' has undefined position. Will map to Position_Unknown.
> - Player track '57' has undefined team_side. Will map to Team_Unknown.
> - Player track '58' has undefined position. Will map to Position_Unknown.
> - Player track '58' has undefined team_side. Will map to Team_Unknown.
> - Player track '59' has undefined position. Will map to Position_Unknown.
> - Player track '59' has undefined team_side. Will map to Team_Unknown.
> - Player track '60' has undefined position. Will map to Position_Unknown.
> - Player track '60' has undefined team_side. Will map to Team_Unknown.
> - Player track '61' has undefined position. Will map to Position_Unknown.
> - Player track '61' has undefined team_side. Will map to Team_Unknown.
> - Player track '62' has undefined position. Will map to Position_Unknown.
> - Player track '62' has undefined team_side. Will map to Team_Unknown.
> - Player track '63' has undefined position. Will map to Position_Unknown.
> - Player track '63' has undefined team_side. Will map to Team_Unknown.
> - Player track '64' has undefined position. Will map to Position_Unknown.
> - Player track '64' has undefined team_side. Will map to Team_Unknown.
> - Player track '65' has undefined position. Will map to Position_Unknown.
> - Player track '65' has undefined team_side. Will map to Team_Unknown.
> - Player track '66' has undefined position. Will map to Position_Unknown.
> - Player track '66' has undefined team_side. Will map to Team_Unknown.
> - Player track '67' has undefined position. Will map to Position_Unknown.
> - Player track '67' has undefined team_side. Will map to Team_Unknown.
> - Player track '68' has undefined position. Will map to Position_Unknown.
> - Player track '68' has undefined team_side. Will map to Team_Unknown.
> - Player track '69' has undefined position. Will map to Position_Unknown.
> - Player track '69' has undefined team_side. Will map to Team_Unknown.
> - Player track '70' has undefined position. Will map to Position_Unknown.
> - Player track '70' has undefined team_side. Will map to Team_Unknown.
> - Player track '71' has undefined position. Will map to Position_Unknown.
> - Player track '71' has undefined team_side. Will map to Team_Unknown.
> - Player track '72' has undefined position. Will map to Position_Unknown.
> - Player track '72' has undefined team_side. Will map to Team_Unknown.
> - Player track '73' has undefined position. Will map to Position_Unknown.
> - Player track '73' has undefined team_side. Will map to Team_Unknown.
> - Player track '74' has undefined position. Will map to Position_Unknown.
> - Player track '74' has undefined team_side. Will map to Team_Unknown.
> - Player track '75' has undefined position. Will map to Position_Unknown.
> - Player track '75' has undefined team_side. Will map to Team_Unknown.
> - Player track '76' has undefined position. Will map to Position_Unknown.
> - Player track '76' has undefined team_side. Will map to Team_Unknown.
> - Player track '77' has undefined position. Will map to Position_Unknown.
> - Player track '77' has undefined team_side. Will map to Team_Unknown.
> - Player track '78' has undefined position. Will map to Position_Unknown.
> - Player track '78' has undefined team_side. Will map to Team_Unknown.
> - Player track '79' has undefined position. Will map to Position_Unknown.
> - Player track '79' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.